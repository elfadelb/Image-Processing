import cv2
import numpy as np

def contraharmonic_mean(img, size, Q):
    numerator = np.sum(np.power(img, Q + 1))
    denominator = np.sum(np.power(img, Q))
    filtered_img = numerator / denominator
    return filtered_img.astype(np.uint8)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
filtered_img = contraharmonic_mean(img, size=3, Q=1.5)

cv2.namedWindow('Contraharmonic Mean', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Contraharmonic Mean', 400, 300)

cv2.imshow('Contraharmonic Mean', filtered_img)
cv2.waitKey(0)
