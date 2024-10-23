import cv2
import numpy

img = cv2.imread("fruit.jpg")

gray = cv2.imread("fruit.jpg", cv2.IMREAD_GRAYSCALE)

cv2.imwrite("gray_img.jpg",gray)
#cv2.imshow("fruit.jpg",img)
cv2.imshow("fruit.jpg",gray)
cv2.waitKey(0)
cv2.destroyAllWindows()