import cv2

img = cv2.imread("fruit.jpg")
#box_blurred = cv2.blur(img, (5,5))

gauss_blurred = cv2.GaussianBlur(img,(111,111),0)
# Display the final result
cv2.imshow("Processed Image", gauss_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
