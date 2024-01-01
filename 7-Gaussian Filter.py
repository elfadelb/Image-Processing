import cv2

def gaussian_filter(img, sigma=1.0):
    return cv2.GaussianBlur(img, (0, 0), sigma)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
filtered_img = gaussian_filter(img, sigma=1.5)

cv2.namedWindow('Gaussian Filter', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Gaussian Filter', 400, 300)

cv2.imshow('Gaussian Filter', filtered_img)
cv2.waitKey(0)
