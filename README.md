# OpenCV-Journal-Part-1

## lab1 ##
Sucessfully pip OpenCV with python3. I also learned how to create an virtual environment. So far it seems to work and does not have other impacts, expect for Github pushes that seems to failn. Virtual environmemt does not allow interactions with cloud services, as it seems.

## lab2 ##

## lab3 ##

## lab4 ##
I was playing with and researching about the parameters of cv2.cornerHarris(), SIFT and FLANN. Here's the interesting findings:
Harris corner detection
blockSize: size of the neighborhood considered for corner detection. >1 integer. Larger values means larger neighborhood size, which can make the function less sensitive to smaller corners. Smaller values make the function sensitive to high-frequency corners.
ksize: Sobel kernel, an positive odd number. ksize must be odd because an even kernel lacks middle element as a reference point, hence symmetry is disrupted.
k: known as freeParameter, is between 0.04 and 0.06; higher value increases possibility of detecting a pt as a corner hence more false positives。

SIFT
nfeatures: Limits the number of features detected. Fewer features for faster processing.
contrastThreshold: Filters out weak features in low-contrast regions.
edgeThreshold: Removes features that are edge-like, ensuring features are more distinct.

FLANN
trees: Controls the precision and memory usage of the algorithm.
checks: Affects the accuracy and speed of the search by setting how many leaf nodes to visit.

Matching
distance ratio is typically <0.7 to filter reliable matches


## lab5 ##
Histograms: graphical representation of the distribution of pixel intensities (ranging from 0 to 255) across an image. This should be useful analyzing color distribution in image processing,.
Channels: to my suprise, each primary color channel (red, green, blue) is analyzed separately. Note that the primary color channels are based on light, not the red, yellow blue based on traditional coloring.
Bins: Set to 256, guaranteed to represent every possible pixel value from 0 to 255. Each pixel can take in an 8-bit image.
Grayscale historgram only has one channel representing light intensity from 0 to 255.
Good recap to use the Matplotlib.


## lab6 ##
Gaussian blur:
Gaussian blur is a method where a bell-shaped curve is used to calculate the weights assigned to neighboring pixels.
ksize is required to be odd too as we have seen in Harris Corner Dection, with respect to the need for symmetry around a central pixel, the filter then can apply transformation symmetrically across the image. The kernel is designed to give more weight to the pixles closer to the center kernel.
The sigmaX value following the kernel size in the Gaussian blur function represents the spread of the Gaussian kernal alone the X-axis, or how much of the neighboring pixels influence the center pixel's final value. Larger sigmaX values results in a wider bell curve, and that the pixels farther away from the center have a more significant impact on the blur, resulting softer blur where details are more smoothed out. Smaller values on the other hand, leads to a narrow bell curve and result in sharper image, blur less prominant and the details more preserved.
Interestingly, ksize and sigmaX are interdependent. Typically sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
or we can set sigma X to 0 so OpenCV would automatically calculate the proper value based on given kernel size.