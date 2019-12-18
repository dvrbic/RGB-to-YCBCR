import cv2
import numpy as np

def rgb_to_ycrbr(image):
    img = (image.astype(float)/255)
    YCbCr_img = np.empty((img.shape[0], img.shape[1], 3), float)
    Y = np.empty([img.shape[0],img.shape[1]], dtype = float)
    Cb = np.empty([img.shape[0],img.shape[1]], dtype = float)
    Cr = np.empty([img.shape[0],img.shape[1]], dtype = float)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            Y[i,j] = (0.299)*(img[i,j][2]) + (0.587)*(img[i,j][1]) + (0.114)*(img[i,j][0])
            Cb[i,j] = (-0.1687)*(img[i,j][2]) + (-0.3313)*(img[i,j][1]) + (0.5)*(img[i,j][0])
            Cr[i,j] = (0.5)*(img[i,j][2]) + (-0.4187)*(img[i,j][1]) + (-0.0813)*(img[i,j][0])
    #img_new = cv2.merge((Cr*255, Cb*255, Y*255))
    YCbCr_img[...,0] = Cr*255
    YCbCr_img[...,1] = Cb*255
    YCbCr_img[...,2] = Y*255
    return YCbCr_img

img = cv2.imread('mandrill.png',1)
out = rgb_to_ycrbr(img)
cv2.imwrite('YCrBrImg.png',out)

def ycrbr_to_rgb(image):
    img = (image.astype(float)/255)
    RGB_img = np.empty((img.shape[0], img.shape[1], 3), float)
    r = np.empty([img.shape[0],img.shape[1]], dtype = float)
    g = np.empty([img.shape[0],img.shape[1]], dtype = float)
    b = np.empty([img.shape[0],img.shape[1]], dtype = float)
    for i in range(image.shape[0]):
        for j in range(image.shape[1]):
            r[i,j] = (1)*(img[i,j][2]) + (0)*(img[i,j][1]) + (1.402)*(img[i,j][0])
            g[i,j] = (1)*(img[i,j][2]) + (-0.34414)*(img[i,j][1]) + (-0.71414)*(img[i,j][0])
            b[i,j] = (1)*(img[i,j][2]) + (1.772)*(img[i,j][1]) + (0)*(img[i,j][0])
    #img_new = cv2.merge((b*255, g*255, r*255))
    RGB_img[...,0] = b*255
    RGB_img[...,1] = g*255
    RGB_img[...,2] = r*255
    return RGB_img
RGBImg = ycrbr_to_rgb(out)
cv2.imwrite('RGBImg.png',RGBImg)