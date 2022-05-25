#!/usr/local/bin/python3
import matplotlib.pyplot as plt
img = plt.imread("cat.png")
plt.imshow(img, interpolation="nearest")
plt.show()
