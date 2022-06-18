"""Main module."""

from PIL import Image
import os


class Img:
    """Class for modification of images using PIl and opencv"""
    def __init__(self, image, filename=None):
        self.image = image
        self.filename = filename
        self.name, self.ext = os.path.splitext(self.image)
        self.pil_image = Image.open(image)
        self.modes = ['L', 'P', 'RGB', 'RGBA', 'CMYK', 'YCbCr', 'LAB', 'HSV', 'I', 'F']

    def save_image(self, img):
        """save image to a new filename or same filename"""
        if self.filename is not None:
            img.save(self.filename)
        else:
            img.save(f"{self.name}{self.ext}")
        return img

    def convert(self, mode='RGB'):
        """convert image mode"""
        if mode not in self.modes:
            raise ValueError("Please provide correct image mode value. To check available modes use Img.help('mode')")

        elif mode == 'RGB':
            pil_image = self.pil_image.convert('RGB')
            return self.save_image(pil_image)
        elif mode == 'RGBA':
            pil_image = self.pil_image.convert('RGBA')
            return self.save_image(pil_image)

        elif mode != 'RGB' or mode != 'RGBA':
            if mode in self.modes:
                print('This mode will be included in future updates')


def im_help(help_for='mode'):
    if help_for == 'mode':
        print('Available image modes are: L, P, RGB, RGBA, CMYK, YCbCr, LAB, HSV, I, F')
