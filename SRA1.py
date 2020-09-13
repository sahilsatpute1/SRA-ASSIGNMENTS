#No bound
from PIL import Image
import numpy as np
#import matplotlib.pyplot as plt

im = Image.open("SRA1.png")

array = np.asarray(im)
#print(type(array))
#print(array.shape)
#print(array)

angle = float(input("enter the angle by which you want to rotate: "))
#a = np.array([angle])
sin = np.sin(angle*np.pi/180)
cos = np.cos(angle*np.pi/180)

#print(sin)
#print(cos)

#b = np.array([[[cos,sin,0],[-sin,cos,0],[0,0,1]]])

T_pos = np.array([[1,0,1000], [0,1,1000], [0,0,1]])      #Translate the image by (1000,1000) since scaling factor is 2 and initially image 
                                                         #image was translated to (-500, -500)

T_rotate = np.array([[cos,sin,0], [-sin,cos,0], [0,0,1]])     #rotating the image ccw by given angle

T_scale = np.array([[2,0,0], [0,2,0], [0,0,1]])      #Scaling the image by factor of 2

T_neg = np.array([[1,0,-500], [0,1,-500], [0,0,1]])  #To translate the center of the image to (-500,-500)

T = T_pos @ T_rotate @ T_scale @ T_neg    

T_inv = np.linalg.inv(T)  #To find inverse of arrays

#Only first six values of the affine transformation matrix is being taken
img_transformed = im.transform((2000, 2000), Image.AFFINE, data=T_inv.flatten()[:6], resample=Image.NEAREST) 
final = np.asarray(img_transformed)  #To get array of the transformed image
final = Image.fromarray(final)  #Converting array to image
final.save("SRA(1).png")
final.show()
#c = np.multiply(b, array)
#print(c)
