import cv2

img = cv2.imread("fruit.jpg")
box_blurred = cv2.blur(img, (5,5))

gauss_blurred = cv2.GaussianBlur(img,(11,11), 11)

median_blurred = cv2.medianBlur(img,13)

bilateral_blurred = cv2.bilateralFilter(img, 33, 25, 25)

# Display the final result
#cv2.imshow("Processed Image", box_blurred)
#cv2.imshow("Processed Image", gauss_blurred)
#cv2.imshow("Processed Image", median_blurred)
cv2.imshow("Processed Image", bilateral_blurred)
cv2.waitKey(0)
cv2.destroyAllWindows()
