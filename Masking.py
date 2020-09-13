import cv2
import numpy as np
from PIL import Image

im = Image.open("SRA5.jpg")
array = np.array(im)
r,c,ch = array.shape
copy = array.copy()  #To convert rgb to bgr i created a new array image of same dimensions

#converting rgb to bgr
for i in range(array.shape[0]):
	for j in range(array.shape[1]):
		copy[i][j][2] = array[i][j][0]
		copy[i][j][1]= array[i][j][1]
		copy[i][j][0] = array[i][j][2]

#converting to hsv colorspace
hsv = cv2.cvtColor(copy, cv2.COLOR_BGR2HSV)

#Define range of blue colour in hsv
lower_blue = np.array([105, 33, 33])
upper_blue = np.array([140, 255, 255])

def masking(hsv, lower_blue, upper_blue):
	r,c,ch = hsv.shape
	mask = np.zeros((r,c,ch), dtype = np.uint8)
	for i in range(r):
		for j in range(c):
			if hsv[i][j][0] >= lower_blue[0] and hsv[i][j][1] >= lower_blue[1] and hsv[i][j][2] >= lower_blue[2] and hsv[i][j][0] <= upper_blue[0] and hsv[i][j][1] <= upper_blue[1] and hsv[i][j][2] <= upper_blue[2]:
				mask[i][j][0] = hsv[i][j][0]
				mask[i][j][1] = hsv[i][j][1]
				mask[i][j][2] = hsv[i][j][2]
	return mask

def bitwise_and(im, mask):
	final = np.bitwise_and(mask, im)
	return final

mask = masking(hsv, lower_blue, upper_blue)
final = bitwise_and(array, mask)
final = Image.fromarray(final)
final.save("masking.jpg")
final.show()
