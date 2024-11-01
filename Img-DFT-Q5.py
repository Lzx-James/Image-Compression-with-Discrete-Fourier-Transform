# a)
import matplotlib.pyplot as plt
import numpy as np

IMG = plt.imread('.\\baboon.png')

# b)
IMG = np.clip(IMG, 0, 1)

# c)

red_channel = IMG[:, :, 0]
green_channel = IMG[:, :, 1]
blue_channel = IMG[:, :, 2]

# DFT for each color channel
DFT_raw = np.fft.fft2(IMG)
red_dft_raw = np.fft.fft2(red_channel)
green_dft_raw = np.fft.fft2(green_channel)
blue_dft_raw = np.fft.fft2(blue_channel)

# d)
# Shift the zero frequency component for each color channel
DFT_coefficient = np.fft.fftshift(DFT_raw)
red_coefficient = np.fft.fftshift(red_dft_raw)
green_coefficient = np.fft.fftshift(green_dft_raw)
blue_coefficient = np.fft.fftshift(blue_dft_raw)

# e)
# Get the magnitude of each color channel
DFT_magnitude = np.abs(DFT_coefficient)
red_magnitude = np.abs(red_coefficient)
green_magnitude = np.abs(green_coefficient)
blue_magnitude = np.abs(blue_coefficient)

# f) g)
R = {0.001, 0.003, 0.01, 0.03}
# r will be selected in {0.001, 0.003, 0.01, 0.03}

def DFT_Compress_iDFT(Channel, Magnitude_2d, compress_ratio):
    Magnitude_1d = Magnitude_2d.ravel()

    # h)
    coefficient_to_keep_ratio = int(compress_ratio * len(Magnitude_1d))
    sort_array = np.sort(Magnitude_1d)[::-1]
    coefficient_to_keep = sort_array[coefficient_to_keep_ratio]

    DFT_compressed = np.zeros_like(Channel)

    for i in range(Channel.shape[0]):
        for j in range(Channel.shape[1]):
            if np.abs(Channel[i][j]) >= coefficient_to_keep:
                DFT_compressed[i][j] = Channel[i][j]

    # i)
    DFT_coefficient_new = np.fft.ifftshift(DFT_compressed)

    # j)
    Channel_iDFT = np.fft.ifft2(DFT_coefficient_new).real

    # k)
    return Channel_iDFT


# l)

for r in R:
    # Call the compress function for each Color Channel
    red_channel = DFT_Compress_iDFT(Channel=red_coefficient, Magnitude_2d=red_magnitude, compress_ratio=r)
    green_channel = DFT_Compress_iDFT(Channel=green_coefficient, Magnitude_2d=green_magnitude, compress_ratio=r)
    blue_channel = DFT_Compress_iDFT(Channel=blue_coefficient, Magnitude_2d=blue_magnitude, compress_ratio=r)

    # Synthesize the new compressed image
    IMG_new = np.stack((red_channel, green_channel, blue_channel), axis=-1)

    # Normalize the image
    # IMG_new = (IMG_new - IMG_new.min()) / (IMG_new.max() - IMG_new.min())
    IMG_new = np.clip(IMG_new, 0, 1)

    # Display the image
    plt.imshow(IMG_new)
    plt.show()

    # Compute the mean squared error between the original and compressed image
    mse = np.mean((IMG - IMG_new) ** 2)
    print('Compress Ratio:', r, 'MSE:', mse)

    # Save the image
    plt.imsave('compressed_image\\baboon_ratio={:.3f}_mse={:.5f}.png'.format(r, mse), IMG_new)
