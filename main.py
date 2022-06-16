# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
# git提交代码跳过ssl验证
##git config --global http.sslVerify false
import os
import numpy as np
import cv2 as cv
import shutil
from BatchRename import BatchRename



def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


if __name__ == '__main__':
    print_hi('PyCharm')
    demo = BatchRename()
    demo.rename()











# from matplotlib import pyplot as plt
#
# img = cv.imread('test.jpg',0)
# edges = cv.Canny(img, 100, 200)
#
# plt.subplot(121),plt.imshow(img,cmap = 'gray')
# plt.title('Original Image'), plt.xticks([]), plt.yticks([])
# plt.subplot(122),plt.imshow(edges,cmap = 'gray')
# plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
#
# plt.show()

