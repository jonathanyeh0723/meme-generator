from email_function import Email
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator

import os
import random
import argparse


def generate_meme(path=None, body=None, author=None):
    """Generate a meme given an path and a quote."""
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/picked/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
        img = path

    if body is None:
        quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv',
                       './_data/CatQuotes/CatQuotesTXT.txt',
                       './_data/CatQuotes/CatQuotesPDF.pdf',
                       './_data/CatQuotes/CatQuotesDOCX.docx',
                       './_data/CatQuotes/CatQuotesCSV.csv']
        quotes = []
        for f in quote_files:
            quotes.extend(Ingestor.parse(f))

        quote = random.choice(quotes)
    else:
        if author is None:
            raise Exception('Author Required if Body is Used')
        quote = QuoteModel(body, author)

    meme = MemeGenerator('./tmp')
    output = meme.make_meme(img, quote.body, quote.author)
    return output


if __name__ == "__main__":
    meme = MemeGenerator('./static')
    #print(type(meme))
    output = meme.make_meme('./_data/photos/picked/neymar_1.jpg', 'Hi there', 'Jonathan')
    print(Email.send('johnnyyeh0723@gmail.com', 'Send email with image test', 'Hi there', output))
