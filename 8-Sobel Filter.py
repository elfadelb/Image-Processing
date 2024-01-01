import cv2

def sobel_filter(img):
    return cv2.Sobel(img, cv2.CV_64F, 1, 1, ksize=3)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
filtered_img = sobel_filter(img)

cv2.namedWindow('Sobel Filter', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Sobel Filter', 400, 300)

cv2.imshow('Sobel Filter', filtered_img)
cv2.waitKey(0)
