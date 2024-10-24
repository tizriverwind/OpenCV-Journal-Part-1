# OpenCV-Journal-Part-1

## lab1 ##
Successfully installed OpenCV using pip alongside Python 3. Created a virtual environment to isolate and manage Python packages specific to this project. The virtual environment appears to restrict or complicate interactions with cloud services like GitHub, but I was able to push changes after terminating the virtual environment.


## lab2 ##
Color images use multiple color channels to represent color; grayscale images use only one channel ranging from black to white. The definition of a grayscale imgae is quite literally, 50 (or more) shades of gray.
Jokes aside, I found the conversion from colorful to grayscale quite interesting. The typical conversion process eliminates the hue and saturation from a pixel while maintaining its luminance (fancy word!). 
Another interesting fact I discovered researching about RGB and grayscales, is that human perceived the color green much more prominently than red and blue so this needs to be taken into consideration in conversion.
Grayscale images are often used in edge detecting, thresholding, feature extractions and so on. It is simpler and faster to perform Computer Vision processes on a grayscale image than a color image. 


## lab3 ##
cv2.rectangle (image, (x1, y1), (x2, y2), (color), thickness)
cv2.circle (image, (center x, center y), radius, (color), thickness)
cv2.putText(image, ‘text’, (x, y), font, fontScale, (color), thickness)
cv2.getRotationMatrix2D(center, angle, scale)
    Center: center coordinates (x, y)
    Angle is positive for anti-clockwise(surprised!) and negative for clockwise
    Scale: scaling factor

HSV (Hue-Saturation-Value)
Interesting concept. Artists might be more familiar with? 
Hue - color type, runs from 0 to 360. Scaled to 0-179 in OpenCV library.
Saturation - intensity of purity of the color. 0%(gray) or 0 - 100% or 255(full color intensity)
Value - brightness. 0%(black) or 0 - 100% or 255(brightest, or white)
I'd imagine HSV would be useful in color filtering.


## lab4 ##

I was playing with and researching about the parameters of cv2.cornerHarris(), SIFT and FLANN. Here's the interesting findings:

Harris Corner Detection
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
cv2.GaussianBlur(input img, (ksize), sigmaX)
Gaussian blur is a method where a bell-shaped curve is used to calculate the weights assigned to neighboring pixels.
ksize is required to be odd too as we have seen in Harris Corner Dection, with respect to the need for symmetry around a central pixel, the filter then can apply transformation symmetrically across the image. The kernel is designed to give more weight to the pixles closer to the center kernel.
The sigmaX value following the kernel size in the Gaussian blur function represents the spread of the Gaussian kernal alone the X-axis, or how much of the neighboring pixels influence the center pixel's final value. Larger sigmaX values results in a wider bell curve, and that the pixels farther away from the center have a more significant impact on the blur, resulting softer blur where details are more smoothed out. Smaller values on the other hand, leads to a narrow bell curve and result in sharper image, blur less prominant and the details more preserved.
Interestingly, ksize and sigmaX are interdependent. Typically sigma = 0.3*((ksize-1)*0.5 - 1) + 0.8
or we can set sigma X to 0 so OpenCV would automatically calculate the proper value based on given kernel size.
I tested several different combinations of ksize and sigmaX values just to see different blurring affects.

cv2.medianBlue(input img, ksize)
Applying a median blur filter transforms the image in a way reminiscent of pixel art in my opinion. This filter reduces noise by replacing each pixel's value with the median value of the intensities in the neighborhood defined by ksize. The resultant hard edges and block-like appearance are characteristic of pixel art.

cv2.bilateralFilter(input img, diameter, sigmaColor, sigmaSpace)
Bilateral filtering reminds me of the beauty filters used on socail media platforms. It seems to blur"imperfections" in the image while keep true to the details (as it should, as bilateral filtering usually considers both pixel intensity differences and sptial proximity to preserves edges)
diameter = diameter of the pixel neighborhood
higher value of sigmaColor = more blurring effect
higher value of sigmaSpace = more spatial smoothing
