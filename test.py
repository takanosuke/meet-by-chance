import cv2
from matplotlib import pyplot as plt
import random
 
# カラー画像の読み込み
img = cv2.imread('test.jpeg', 1)
 
# グレースケール化
img_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
 
# 単純二値化
ret, img_binary = cv2.threshold(img_gray,
                                60, 255,
                                cv2.THRESH_BINARY)
# 輪郭抽出
contours, hierarchy = cv2.findContours(img_binary,
                                       cv2.RETR_LIST,
                                       cv2.CHAIN_APPROX_NONE)
# 輪郭を元画像に描画
for i, cnt in enumerate(contours):
    g = random.randint(0, 255)
    r = random.randint(0, 255)
    b = random.randint(0, 255)
    img_contour = cv2.drawContours(img, contours, -1, (r, g, b), -1)

# ここから画像描画
fig = plt.figure()
ax1 = fig.add_subplot(111)
ax1.imshow(cv2.cvtColor(img_contour, cv2.COLOR_BGR2RGB))
ax1.axis('off')
plt.show()
plt.close()