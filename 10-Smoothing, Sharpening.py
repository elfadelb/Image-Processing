import cv2

def smoothing(img, kernel_size=3):
    return cv2.blur(img, (kernel_size, kernel_size))

def sharpening(img, alpha=1.5):
    blurred = cv2.GaussianBlur(img, (0, 0), 1.0)
    sharpened = cv2.addWeighted(img, alpha, blurred, 1 - alpha, 0)
    return sharpened

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
smoothed_img = smoothing(img, kernel_size=5)
sharpened_img = sharpening(smoothed_img, alpha=1.5)

cv2.namedWindow('Smoothing', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Smoothing', 400, 300)

cv2.namedWindow('Sharpening', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Sharpening', 400, 300)

cv2.imshow('Smoothing', smoothed_img)
cv2.imshow('Sharpening', sharpened_img)
cv2.waitKey(0)
