import cv2
import numpy as np

img = cv2.imread("fruit.jpg")
gray = cv2.imread("fruit.jpg", cv2.IMREAD_GRAYSCALE)

# harris corner
gray_f = np.float32(gray)
hc = cv2.cornerHarris(gray,blockSize=5,ksize=3,k=0.05)

# Dilate the detected corners to enhance them
hc_dilated = cv2.dilate(hc, None)
hc_img = np.copy(img)
hc_img[hc_dilated > 0.01 * hc_dilated.max()] = [0,0,255]

# keypoint detector SIFT
sift1 = cv2.SIFT_create()
keypoints, descriptors = sift1.detectAndCompute(gray, None)

# Mark the keypoints
img_with_lines = cv2.drawKeypoints(img, keypoints, None, flags= cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

# Matching with FLANN: MONA LISA 
img1 = cv2.imread("MonaLisa.jpg",cv2.IMREAD_GRAYSCALE)
img2 = cv2.imread("ml_museum.jpg",cv2.IMREAD_GRAYSCALE)

# Sift and FLANN
sift2 = cv2.SIFT_create()
keypoints1,descriptors1 = sift1.detectAndCompute(img1, None)
keypoints2,descriptors2 = sift1.detectAndCompute(img2, None)

FLANN_INDEX_KDTREE = 1
index_param = dict(algorithm=FLANN_INDEX_KDTREE,trees=5)
search_param = dict(checks=50)
flann = cv2.FlannBasedMatcher(index_param,search_param)
matches = flann.knnMatch(descriptors1,descriptors2,k=2)

# good matches
gm = []
for m, n in matches:
    if m.distance < 0.7*n.distance:
        gm.append(m)

# connecting matches with lines
result = cv2.drawMatches(img1, keypoints1, img2, keypoints2, gm, None, 
                         flags=cv2.DRAW_MATCHES_FLAGS_NOT_DRAW_SINGLE_POINTS)

# Display the final result
cv2.imshow("Harris-Corners", hc_img)
cv2.imshow("SIFT Image", img_with_lines)
cv2.imshow("Feature matching", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
