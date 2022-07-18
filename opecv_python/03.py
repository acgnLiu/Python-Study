import cv2
import numpy as np

# import os

file1 = "1.jpg"
file2 = "2.jpg"

image1 = cv2.imread(file1)
image2 = cv2.imread(file2)
difference = cv2.subtract(image1, image2)
print(difference)
result = not np.any(difference)  # if difference is all zeros it will return False

if result is True:
    print("两张图片一样")
else:
    cv2.imwrite("result.jpg", difference)
    print("两张图片不一样")

