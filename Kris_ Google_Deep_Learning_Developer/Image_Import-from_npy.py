# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 12:29:16 2020

@author: VK
"""

from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


# https://teachablemachine.withgoogle.com/

#Exxport the model from teachablemachine ie, .h5 file

#https://www.electronjs.org/apps/netron
#Open netron and export part of CON2D 


imag_array = np.load("expanded_conv_project_kernel_0.npy")

imag_array


#im = Image.fromarray(imag_array[0][1])
im = Image.fromarray(imag_array.astype(np.uint8))

im.show()


from IPython.display import Image
Code_numpy_import = Image("Code_to_Import_npy.JPG")
Code_numpy_import