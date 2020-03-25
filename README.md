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
入力画面の一例

<img src="https://user-images.githubusercontent.com/41196217/75736198-e7b5de00-5d3f-11ea-9ca0-f4637a5d5588.png" width="480px">

出力画面の一例

<img src="https://user-images.githubusercontent.com/41196217/75736263-12079b80-5d40-11ea-88f6-5f67553e0556.png" width="480px">

## Usage
ターミナル上で次のコマンドを実行してください
```
- set FLASK_APP=predict_file.py
- python -m flask run --withoutthreads
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
