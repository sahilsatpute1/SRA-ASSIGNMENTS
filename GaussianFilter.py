from PIL import Image
import numpy as np

im = Image.open("SRA2(2).png")
array =  np.array(im)
kernel = np.array([[1/273, 4/273, 7/273, 4/273, 1/273], [4/273, 16/273, 26/273, 16/273, 4/273], [7/273, 26/273, 41/273, 26/273, 7/273], [4/273, 16/273, 26/273, 16/273, 4/273], [1/273, 4/273, 7/273, 4/273, 1/273]])
ri,ci,chi = array.shape


def convolve(im, kernel):
	new_im = np.zeros_like(array)
	pad_image = np.zeros((array.shape[0] + 4, array.shape[1] + 4, array.shape[2]))
	pad_image[2:-2, 2:-2, : ] = array

	for i in range(ci):
		for j in range(ri):
			for k in range(chi):
				new_im[j, i, k] = (kernel * pad_image[j:j+5, i:i+5, k]).sum()
	return new_im

			
final = convolve(im, kernel)
final = Image.fromarray(final)
final.save("SRA2((2)).png")
final.show()