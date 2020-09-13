from PIL import Image
import numpy as np

im = Image.open("SRA3(1).png")
array =  np.array(im)
kernel = np.array([[-1, 0, 1], [-1, 0, 1], [-1, 0, 1]])
ri,ci,chi = array.shape


def convolve(im, kernel):
	new_im = np.zeros_like(array)
	pad_image = np.zeros((array.shape[0] + 2, array.shape[1] + 2, array.shape[2]))
	pad_image[1:-1, 1:-1, : ] = array

	for i in range(ci):
		for j in range(ri):
			for k in range(chi):
				new_im[j, i] = (kernel * pad_image[j:j+3, i:i+3, k]).sum()
	return new_im
			
final = convolve(im, kernel)
final = Image.fromarray(final)
final.save("vertical.png")
final.show()