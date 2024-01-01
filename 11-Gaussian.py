import cv2

def apply_gaussian(img, sigma=1.0):
    return cv2.GaussianBlur(img, (0, 0), sigma)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
blurred_img = apply_gaussian(img, sigma=1.5)  

cv2.namedWindow('Gaussian', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Gaussian', 400, 300)

cv2.imshow('Gaussian', blurred_img)
cv2.waitKey(0)
