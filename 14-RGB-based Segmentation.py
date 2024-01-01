import cv2
import numpy as np

def rgb_segmentation(img, lower_threshold, upper_threshold):
    segmented_img = cv2.inRange(img, lower_threshold, upper_threshold)
    return segmented_img

img = cv2.imread('Images/dog-color.jpg')
lower_threshold = np.array([100, 50, 50])
upper_threshold = np.array([140, 255, 255])
segmented_img = rgb_segmentation(img, lower_threshold, upper_threshold)

cv2.namedWindow('RGB Segmentation', cv2.WINDOW_NORMAL)
cv2.resizeWindow('RGB Segmentation', 400, 300)

cv2.imshow('RGB Segmentation', segmented_img)
cv2.waitKey(0)
