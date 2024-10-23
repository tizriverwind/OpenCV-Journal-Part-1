import cv2
import numpy as np
import matplotlib.pyplot as plt

img = cv2.imread("MonaLisa.jpg")
# hist = cv2.calcHist([img],[0],None, [256],[0,256])
channels = ("b","g","r")

for i, col in enumerate(channels):
    hist_color = cv2.calcHist([img],[i], None, [256], [0,256])
    plt.plot(hist_color,color = col)

# Display the final result
plt.title("Mona Lisa")
plt.xlabel("Pixel Intensity")
plt.ylabel("Frequency")
plt.show()