import cv2
import numpy as np

def bit_plane_slicing(img, bit):
    return (img >> bit) & 1

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
sliced_img = bit_plane_slicing(img, 7)

cv2.namedWindow('Bit Plane Slicing', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Bit Plane Slicing', 400, 300)

cv2.imshow('Bit Plane Slicing', sliced_img * 255)
cv2.waitKey(0)