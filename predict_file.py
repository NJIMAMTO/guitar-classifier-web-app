import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

#=======#ダミーデータ#=======#
x = [1, 2, 3, 4, 5]
y = [99.0, 45.3, 22.1, 1.0, 8.5]
label_x = ["A", "B", "C", "D", "E"]

road_image = Image.open("test.jpg")
rgb_img = road_image.convert('RGB')

#=======#プロットして保存する#=======#
fig = plt.figure(figsize=(10.25, 5.12))

#=======#棒グラフを書く#=======#
ax1 = fig.add_subplot(1,2,1)
ax1.barh(
        x,
        y, 
        color='c',
        align="center")
ax1.set_yticks(x, label_x)#y軸のラベル
ax1.set_xticks([])#x軸のラベルを消す

# 棒グラフ内に数値を書く
for interval, Y in zip(range(1,len(y)+1), y):
    ax1.text(10.0, interval, Y, ha='left', va='center')

#=======#判別した画像を入れる#=======#
ax2 = fig.add_subplot(1,2,2)
ax2.imshow(rgb_img)
ax2.axis('off')

plt.show()