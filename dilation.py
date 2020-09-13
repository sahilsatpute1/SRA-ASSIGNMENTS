from PIL import Image
import numpy as np

im = Image.open("SRA4.png")
array =  np.array(im)
kernel = np.array([[1, 1, 1], [1, 1, 1], [1, 1, 1]])
ri,ci,chi = array.shape

for i in range(array.shape[1]):
	for j in range(array.shape[0]):
		for k in range(array.shape[2]):
			if array[j,i,k] >  250:
				array[j,i,k] = 1
			elif array[j,i,k] <= 250:
				array[j,i,k] = 0

def convolve(im, kernel):
	new_im = np.zeros_like(array)
	pad_image = np.zeros((array.shape[0] + 2, array.shape[1] + 2, array.shape[2]))
	pad_image[1:-1, 1:-1, : ] = array

	for i in range(ci):
		for j in range(ri):
			for k in range(chi):
				if (kernel * pad_image[j:j+3, i:i+3, k]).sum() == 0:
					new_im[j,i,k] = 0
				elif (kernel * pad_image[j:j+3, i:i+3, k]).sum() > 0:
					new_im[j,i,k] = 1
	return new_im			


final = convolve(im, kernel)

for i in range(final.shape[1]):
	for j in range(final.shape[0]):
		for k in range(final.shape[2]):
			if final[j,i,k] ==  1:
				final[j,i,k] = 255
			elif final[j,i,k] == 0:
				final[j,i,k] = 0


final = Image.fromarray(final)
final.save("dilation.png")
final.show()