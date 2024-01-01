import cv2
import numpy as np

def contrast_stretching(img, min_out=0, max_out=255):
    min_in, max_in = img.min(), img.max()
    stretched_img = (img - min_in) * ((max_out - min_out) / (max_in - min_in)) + min_out
    return stretched_img.astype(np.uint8)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
stretched_img = contrast_stretching(img)

cv2.namedWindow('Contrast Stretching', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Contrast Stretching', 400, 300)

cv2.imshow('Contrast Stretching', stretched_img)
cv2.waitKey(0)
