import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

def to_graph(image, labels, predicted):
    #=======#プロットして保存する#=======#
    fig = plt.figure(figsize=(10.24, 5.12))
    fig.subplots_adjust(left=0.2)

    #=======#横棒グラフを書く#=======#
    ax1 = fig.add_subplot(1,2,1)
    ax1.barh(labels, predicted, color='c', align="center")
    ax1.set_yticks(labels)#y軸のラベル
    ax1.set_xticks([])#x軸のラベルを消す

    # 棒グラフ内に数値を書く
    for interval, value in zip(range(0,len(labels)), predicted):
        ax1.text(0.02, interval, value, ha='left', va='center')

    #=======#判別した画像を入れる#=======#
    ax2 = fig.add_subplot(1,2,2)
    ax2.imshow(image)
    ax2.axis('off')

    return fig

def expand_to_square(input_file):
    """長方形の画像を正方形に変換する
    input_file: 変換するファイル名
    返り値:     変換された画像
    """
    img = Image.open(input_file)
    img = img.convert("RGB")
    
    width, height = img.size
    #縦長なら横に拡張する
    if width < height:
        result = Image.new(img.mode,(height, height),(255, 255, 255))
        result.paste(img, ((height - width) // 2, 0))
    #横長なら縦に拡張する
    elif width > height:
        result = Image.new(img.mode,(width, width),(255, 255, 255))
        result.paste(img, (0, (width - height) // 2))
    else:
        result = img
    
    return result 