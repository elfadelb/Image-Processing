import cv2
import numpy as np

def opening_closing_operations(img, kernel_size=3):
    kernel = np.ones((kernel_size, kernel_size), np.uint8)
    opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
    closing = cv2.morphologyEx(opening, cv2.MORPH_CLOSE, kernel)
    return opening, closing

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
opened_img, closed_img = opening_closing_operations(img, kernel_size=5)

cv2.namedWindow('Opening', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Opening', 400, 300)

cv2.namedWindow('Closing', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Closing', 400, 300)

cv2.imshow('Opening', opened_img)
cv2.imshow('Closing', closed_img)
cv2.waitKey(0)
