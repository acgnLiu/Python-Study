import cv2 as cv
import matplotlib.pyplot as plt
import numpy as np

src = cv.imread("../img/target.jpg")
img = src.copy()
src_roi = cv.imread("../img/template01.jpg")
roi = src_roi.copy()

# 模板匹配
res = cv.matchTemplate(img, roi, cv.TM_CCOEFF_NORMED)

# 返回模板中最匹配的位置，确定左上角的坐标
min_Val, max_Val, min_Loc, max_Loc = cv.minMaxLoc(res)
# 使用相关系数匹配时，最大值为最佳匹配位置
top_left = max_Loc
roi_rows, roi_cols = roi.shape[:2]
cv.rectangle(img, top_left, (top_left[0] + roi_cols, top_left[1] + roi_rows)
             , (0, 0, 255), 3)

# 显示图像
fig, axes = plt.subplots(nrows=2, ncols=2, figsize=(10, 8), dpi=100)
# axes[0][0].imshow(src[:, :, ::-1])
# axes[0][0].set_title("原图")
# axes[0][1].imshow(roi[:, :, ::-1])
# axes[0][1].set_title("模板")
# axes[1][0].imshow(res, cmap=plt.cm.gray)
# axes[1][0].set_title("比较结果")
axes[1][1].imshow(img[:, :, ::-1])
axes[1][1].set_title("最终匹配图")
plt.show()

