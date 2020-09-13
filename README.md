# SRA-ASSIGNMENTS
# Assignments Description:
  We take input image and perform operations like image rotation, blurring and sharpening vertical, horizontal, sobel and canny edge detection, morphological transformations,
  masking, region of interest
# Tools:
Numpy, Pillow and for hsv colospace cv2.cvtColor() is only used.
# 1)Image rotation:
I have tried image rotation using affine transformations, but only for the no bound case. Since pil assumes origin at top left corner of image, i have translated image 
so as to bring origin at centre and also i have scaled image so that after rotation image fits inside the frame.
Rotation matrix used is- [[cos,sin,0], [-sin, cos, 0], [0,0,1]]

# 2)Blurring and sharpening:
a) For gaussian blur, I have used a kernel and then i convolved that kernel(5x5) with my image to get gaussian blur image.
b) For box blur, I have used a kernel(5x5) and applied it on image to get box blur image.
c) For sharpening, I have used a kernel(5x5) and applied it on image to get sharpened image.

# 3)Edge detection:
a) For horizontal and vertical edge detection, I applied 3x3 kernels to the input image to get horizontal and vertical edge detection. 
b) For sobel edge detection, I applied 3x3 kernels to my input image to get sobel edge detection.
c) For canny edge detection, i referred- https://towardsdatascience.com/canny-edge-detection-step-by-step-in-python-computer-vision-b49c3a2d8123 this link helped me understand canny edge detection.

# 4)Morphological Transformations:
a)Erosion and dilation: First of all i converted image to a binary image. Then i convolved the image with kernel such that-
i) For erosion if all the pixels under kernel are 1 then only the pixel value of image will be 1 else zero.
ii) For dilation if at least 1 pixel under kernel is 1 then the pixel value of image will be 1 else zero.
link-https://docs.opencv.org/master/d9/d61/tutorial_py_morphological_ops.html

# 5)Mask:
Here, I converted image from RGB tor BGR and then to HSV. Then we find pixels within range of colour(blue) to be detected ,perform bitwise_and operation in numpy and convert it back to RGB.

# 6) ROI:
With trial and error i found the pixel values of the ball. Then using numpy indexing i extracted the ball portion and converted that to gray and then i found the pixels within the range 
and then using bitwise operations i pasted the roi on the new position in the original image.
link-https://docs.opencv.org/master/d3/df2/tutorial_py_basic_ops.html
link-https://docs.opencv.org/master/d0/d86/tutorial_py_image_arithmetics.html
