import random
import cv2

def add_noise(img):
    row, col = img.shape
    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 255

    number_of_pixels = random.randint(300, 10000)
    for i in range(number_of_pixels):
        y_coord = random.randint(0, row - 1)
        x_coord = random.randint(0, col - 1)
        img[y_coord][x_coord] = 0

    return img

img = cv2.imread('Images/dog.jpg', cv2.IMREAD_GRAYSCALE)
noisy_img = add_noise(img)

cv2.namedWindow('Salt and Pepper', cv2.WINDOW_NORMAL)
cv2.resizeWindow('Salt and Pepper', 400, 300)

cv2.imshow('Salt and Pepper', noisy_img)
cv2.waitKey(0)
