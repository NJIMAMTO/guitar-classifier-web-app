import io
import gc

from flask import Flask, request, redirect, url_for
from flask import flash, render_template, make_response

from keras.models import Sequential, load_model
from keras.applications.resnet50 import decode_predictions
import keras

import numpy as np
from PIL import Image
from matplotlib.backends.backend_agg import FigureCanvasAgg

import graphing

classes = [
            "Fender Stratocaster",
            "Fender Telecaster",
            "Fender Jazzmaster",
            "Fender Jaguar",
            "Fender Mustang",
            "Gibson LesPaul",
            "Gibson SG",
            "Gibson FlyingV",
            "Gibson ES-335",
            "Acoustic guitar"
            ]
num_classes = len(classes)
image_size = 224
ALLOWED_EXTENSIONS = set(['png', 'jpg', 'gif'])


app = Flask(__name__)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.',1)[1].lower() in ALLOWED_EXTENSIONS

@app.route('/', methods=['GET', 'POST'])
def upload_file():
    if request.method == 'POST':
        if 'file' not in request.files:
            flash('ファイルがありません')
            return redirect(request.url)
        file = request.files['file']

        if file.filename == '':
            flash('ファイルがありません')
            return redirect(request.url)

        if file and allowed_file(file.filename):
            virtual_output = io.BytesIO()
            file.save(virtual_output)
            filepath = virtual_output

            model = load_model('./cnn_model/guitar_cnn_resnet50.h5')

            #画像を正方形に変換する
            image = graphing.expand_to_square(filepath)
            image = image.convert('RGB')
            #画像サイズを224x224にそろえる
            image = image.resize((image_size, image_size))
            #画像からnumpy配列に変更し正規化を行う
            data = np.asarray(image) / 255.0
            #配列の次元を増やす(3次元->4次元)
            data = np.expand_dims(data, axis=0)
            #学習したモデルを使って推論をする
            result = model.predict(data)[0]
            
            #推論結果と推論した画像をグラフで描画する
            fig = graphing.to_graph(image, classes, result)
            canvas = FigureCanvasAgg(fig)
            png_output = io.BytesIO()
            canvas.print_png(png_output)
            data = png_output.getvalue()

            response = make_response(data)
            response.headers['Content-Type'] = 'image/png'
            response.headers['Content-Length'] = len(data)

            #推論が終わったらモデルを消去する
            del model
            keras.backend.clear_session()
            gc.collect()

            return response
    return '''
    <!doctype html>
    <html>
        <head>
            <meta charset="UTF-8">
            <title>ファイルをアップロードして判定しよう</title>
        </head>
        <body>
            <h1>ファイルをアップロードして判定しよう！</h1>
            <form method = post enctype = multipart/form-data>
                <p><input type=file name=file>
                <input type=submit value=Upload>
            </form>
        </body>
    </html>
    '''
    