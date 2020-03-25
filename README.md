# ギター分類ウェブアプリ

## Description
- Fender Stratocaster
- Fender Telecaster
- Fender Jazzmaster
- Fender Jaguar
- Fender Mustang
- Gibson LesPaul
- Gibson SG
- Gibson FlyingV
- Gibson ES-335
- Acoustic guitar

を分類してくれる簡易なウェブアプリです。

## Demo
出力ウィンドウの一例

<img src="https://user-images.githubusercontent.com/41196217/77495371-b5555780-6e8b-11ea-9c0c-4dd388339a91.png" width="480px">

## Usage
ターミナル上で次のコマンドを実行してください
```
set FLASK_APP=predict_file.py
python -m flask run --without-threads
```
ローカルホストの127.0.0.1:5000にブラウザ上からアクセスするとページが開き、ギター画像を識別させることが出来ます。

## Install

- Flask
- Keras
- Pillow
- Matplotlib
- Numpy

をpipからインストールする必要があります。

また、別途ダウンロードしたkerasのmodelファイルをこのリポジトリ直下のcnn_modelフォルダに入れておく必要があります。

ダウンロード先↓

https://drive.google.com/open?id=1ZK8yM0QHAOJ1ZCpqz2mYltO_jVm8HYAS
