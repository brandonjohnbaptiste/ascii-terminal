import imageio.v3 as iio
import numpy as np


if __name__ == "__main__":
    img = iio.imread("pineapple.jpg")
    print(f'Image Size: {img.shape[0]} x {img.shape[1]}')
