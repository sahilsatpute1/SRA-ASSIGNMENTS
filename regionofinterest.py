from PIL import Image
import numpy as np

im = Image.open("SRA6(1).jpg")
array = np.array(im)
im_roi = array[880:1040, 1030:1190, : ]

def inverting(array):
	copy = array.copy()
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			array[i][j][2] = copy[i][j][0]
			array[i][j][1] = copy[i][j][1]
			array[i][j][0] = copy[i][j][2]
	return copy

def gray(coloured_image):
	r,g,b = coloured_image[:,:,0], coloured_image[:,:,1], coloured_image[:,:,2]
	gray = 0.2989*r+0.5780*g+0.1140*b
	return gray

def threshold(array, thresh_value, greater_than_thresh_value, less_than_thresh_value):
	copy = np.empty((array.shape[0], array.shape[1], 3), dtype = np.uint8)
	for i in range(array.shape[0]):
		for j in range(array.shape[1]):
			if array[i,j] > thresh_value:
				copy[i,j, : ] = greater_than_thresh_value
			else:
				copy[i,j, : ] = less_than_thresh_value
	return copy

array = inverting(array)
im_roi = inverting(im_roi)

rn,rc,rch = im_roi.shape
roi_x = 850
roi_y = 225
roi = array[roi_x:roi_x+rn, roi_y:roi_y+rc, :]
gray = gray(im_roi)
thresh1 = threshold(gray, 120, 255, 0)
thresh2 = threshold(gray, 100, 0, 255)
mask = np.bitwise_or(thresh1, thresh2)
mask_inv = np.bitwise_not(mask)

im_bg = np.bitwise_and(roi, mask_inv)
im_roi_fg = np.bitwise_and(im_roi, mask)
add = np.bitwise_or(im_bg, im_roi_fg)
array[roi_x:roi_x+rn, roi_y:roi_y+rc, :] = add
final = inverting(array)
final = Image.fromarray(final)
final.save("regionofinterest.jpg")
final.show()