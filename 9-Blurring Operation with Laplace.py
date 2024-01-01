import cv2

def blurring_with_laplace(img, sigma=1.0):
    blurred = cv2.GaussianBlur(img, (0, 0), sigma)
    return cv2.Laplacian(blurred, cv2.CV_64F)

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
filtered_img = blurring_with_laplace(img, sigma=1.5)

cv2.namedWindow('Blurring with Laplace', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Blurring with Laplace', 400, 300)

cv2.imshow('Blurring with Laplace', filtered_img)
cv2.waitKey(0)
