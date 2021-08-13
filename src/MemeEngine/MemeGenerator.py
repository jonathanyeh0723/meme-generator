"""Import libraries for building."""
from PIL import Image, ImageDraw, ImageFont
from random import randint
import os


class MemeGenerator:
    """
    Define MemeGenerator class.

    It needs 1 required positional argument
    for class instantiaion. And a make_meme method
    to generate a meme.
    """

    def __init__(self, output_dir):
        """Class init."""
        self.output_dir = output_dir

    def make_meme(self, img_path, text, author, width=500) -> str:
        """
        Create a meme with text.

        Arguments:
            img_path {str} -- required, the file location for the input image.
            text {str} -- required, text to print on the image.
            author {str} -- required, to indicate text originated.
            width {int} -- optional, to specify requested width size.
        Returns:
            save_path {str} -- saved image path for meme generated.

        """
        self.img_path = img_path
        self.text = text
        self.author = author
        self.width = width

        with Image.open(img_path) as im:

            ratio = self.width/float(im.size[0])
            height = int(ratio*float(im.size[1]))
            im = im.resize((self.width, height), Image.NEAREST)

            draw = ImageDraw.Draw(im)
            font = (ImageFont.truetype(
                './MemeEngine/fonts/LilitaOne-Regular-2.ttf',
                size=20))
            x = randint(0, int(im.size[0]/8))
            y = randint(0, int(im.size[1]/5))
            message = text + '\n' + '    -' + author
            draw.text((x, y), message, font=font, fill=(55, 242, 240))
            save_name = str(randint(0, 1000000)) + '.png'

            if not os.path.exists(self.output_dir):
                try:
                    os.mkdir(self.output_dir)
                except Exception as e:
                    print(e)
            save_path = self.output_dir + '/' + save_name
            im.save(save_path)

        return save_path
