import cv2

def mean_filter(img, kernel_size=3):
    return cv2.blur(img, (kernel_size, kernel_size))

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
filtered_img = mean_filter(img, kernel_size=5)

cv2.namedWindow('Mean Filter', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Mean Filter', 400, 300)

cv2.imshow('Mean Filter', filtered_img)
cv2.waitKey(0)
