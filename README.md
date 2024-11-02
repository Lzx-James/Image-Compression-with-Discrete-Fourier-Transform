# Image-Compression-with-Discrete-Fourier-Transform

A homework of Linear Algebra. Utilized 2D-DFT in Python to transform a 512*512 RGB image and split the color channel. 

## Result

| compress ratio | 0.001   | 0.003   | 0.01    | 0.03    |
| -------------- | ------- | ------- | ------- | ------- |
| MSE            | 0.01553 | 0.01312 | 0.01067 | 0.00816 |

## Analyze

Comparing with original image, the compressed images are more blurry. The compress process only preserved DFT coefficient with top r*100% percent magnitude, and because most of high magnitude components are concentrated in low frequency range, the low magnitude components that are removed are mostly high frequency components. As we all know, high frequency components determine the detail of image, while low frequency components determine geometry. As a result, we will get a blurry image and can’t see the precise detail of image with a lower compress ratio.

A lower compress ratio will lose more detail information of the image. Therefore, the MSE between original image and compressed image will be larger in a lower compress ratio.
