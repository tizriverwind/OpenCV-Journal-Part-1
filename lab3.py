import cv2

# Load images
img = cv2.imread("fruit.jpg")
if img is None:
    print("Error: Image not found")
    exit()

# Resize the image
resized = cv2.resize(img, (540, 720))

# Crop the image
cropped = resized[50:400, 100:650]

# Rotate the cropped image
h, w = cropped.shape[:2]
center = (w // 2, h // 2) # set the center point to have coordinates of half of w and h
matrix = cv2.getRotationMatrix2D(center, 310, 1)  # Rotation by 310 degrees anti-clockwise around the center
rotated = cv2.warpAffine(cropped, matrix, (w, h))

# Convert to HSV color space
hsv = cv2.cvtColor(rotated, cv2.COLOR_BGR2HSV)  # Warning: extremely disturbing color!

# Draw a white line
cv2.line(hsv, (100, 200), (300, 200), (255, 255, 255), 7)

# Draw a circle
cv2.circle(hsv,(290,170),60, (255,0,0),7)

# Draw a rectangle
cv2.rectangle(hsv,(0,0),(200,200), (255,255,0),7)

# Define font for the text
font = cv2.FONT_HERSHEY_SCRIPT_SIMPLEX

# Put text on the image; (x,y) is the bottom-left corner of img
cv2.putText(hsv, "test test", (80, 180), font, fontScale=3, color=(255, 255, 255), thickness=3, lineType=cv2.LINE_AA)

# Display the final result
cv2.imshow("Processed Image", hsv)
cv2.waitKey(0)
cv2.destroyAllWindows()
