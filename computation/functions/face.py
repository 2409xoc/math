#!/usr/local/bin/python3
import cv2, wget, sys
import numpy as np
import matplotlib.pyplot as plt

# i have a dumb idea
## read img -> identify main points -> create f(x) [or multiple f(x) depending on domain] representing the "general" trend of these points -> replot points -> see accuracy (spoiler: not accurate)

# read & show original img
img = cv2.imread("/Users/henry/Downloads/fish.jpeg", cv2.IMREAD_GRAYSCALE)
plt.imshow(img, interpolation="none", cmap="gray")
plt.show()

size = 1
for i in img.shape:
	size *= i
a = np.zeros(size).reshape(img.shape[0], img.shape[1])

