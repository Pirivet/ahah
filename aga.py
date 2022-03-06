import cv2
import numpy as np
import matplotlib.pyplot as plt

image = cv2.imread('tree-with-metadata.jpg')
image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

mask = cv2.threshold(gray, 250, 255, cv2.THRESH_BINARY)[1]
mask = 255 - mask

kernel = np.ones((3,3), np.uint8)
mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN, kernel)
mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE, kernel)
mask = cv2.GaussianBlur(mask, (0,0), sigmaX=2, sigmaY=2,borderType=cv2.BORDER_DEFAULT)
mask = (2*(mask.astype(np.float32))-255.0).clip(0,255).astype(np.uint8)

result = image.copy()
result = cv2.cvtColor(result, cv2.COLOR_BGR2BGRA)
result[:, :, 3] = mask

cv2.imwrite('my_image_without_bckgrnd.png', result)

plt.imshow(image)
plt
