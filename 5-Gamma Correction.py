import cv2
import numpy as np

def gamma_correction(img, gamma=1.0):
    gamma_corrected_img = np.power(img / 255.0, gamma) * 255.0
    return gamma_corrected_img.astype(np.uint8)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
gamma_corrected_img = gamma_correction(img, gamma=1.5)

cv2.namedWindow('Gamma Correction', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Gamma Correction', 400, 300)

cv2.imshow('Gamma Correction', gamma_corrected_img)
cv2.waitKey(0)
