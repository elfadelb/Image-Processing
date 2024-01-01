import cv2

def histogram_equalization(img):
    equalized_img = cv2.equalizeHist(img)
    return equalized_img

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
equalized_img = histogram_equalization(img)

cv2.namedWindow('Histogram Equalization', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Histogram Equalization', 400, 300)

cv2.imshow('Histogram Equalization', equalized_img)
cv2.waitKey(0)