from PIL import Image

"""
File: main.py
Author: Rafal Marguzewicz
Email: info@pceuropa.net
Github: https://github.com/pceuropa/
"""


def watermark_with_transparency(
        base_filename: str="pop.jpg",
        watermark_filename: str="2.jpeg",
        position: tuple=(0, 0)) -> None:

    base_image = Image.open(base_filename).convert('RGBA')
    watermark = Image.open(watermark_filename).convert('RGBA')

    base_image.paste(watermark, position, mask=watermark)
    base_image.save('output.png')


if __name__ == "__main__":
    watermark_with_transparency()