from email_function import Email
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator
from AIEngine import AIEngine

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

def setup():
    """Load all resources."""
    quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                   './_data/DogQuotes/DogQuotesDOCX.docx',
                   './_data/DogQuotes/DogQuotesPDF.pdf',
                   './_data/DogQuotes/DogQuotesCSV.csv',
                   './_data/CatQuotes/CatQuotesTXT.txt',
                   './_data/CatQuotes/CatQuotesPDF.pdf',
                   './_data/CatQuotes/CatQuotesDOCX.docx',
                   './_data/CatQuotes/CatQuotesCSV.csv',
                   './_data/MyQuotes/MyQuotesDOCX.docx',
                   './_data/MyQuotes/MyQuotesCSV.csv']

    quotes = []
    for f in quote_files:
        quotes.extend(Ingestor.parse(f))

    images_path = "./_data/photos/picked/"
    imgs = []
    for root, dirs, files in os.walk(images_path):
        imgs = [os.path.join(root, name) for name in files]

    return quotes, imgs

def meme_rand(quotes, imgs):
    """Generate a random meme."""
    img = random.choice(imgs)
    s3_img = img.split('/')[-1]

    bucket = 'myawsbucket0723'
    cat_bucket = ['neymar_1.jpg', 'neymar_2.jpg',
                  'neymar_3.jpeg', 'neymar_4.jpeg']
    dog_bucket = ['xander_1.jpg', 'xander_2.jpg',
                  'xander_3.jpg', 'xander_4.jpg']
    view_bucket = ['iceland_1.jpeg', 'iceland_2.jpeg',
                   'iceland_3.jpeg', 'iceland_4.jpeg']

    dog_quote_files = ['./_data/DogQuotes/DogQuotesTXT.txt',
                       './_data/DogQuotes/DogQuotesDOCX.docx',
                       './_data/DogQuotes/DogQuotesPDF.pdf',
                       './_data/DogQuotes/DogQuotesCSV.csv']
    dog_quotes = []
    for f in dog_quote_files:
        dog_quotes.extend(Ingestor.parse(f))

    cat_quote_files = ['./_data/CatQuotes/CatQuotesTXT.txt',
                       './_data/CatQuotes/CatQuotesPDF.pdf',
                       './_data/CatQuotes/CatQuotesDOCX.docx',
                       './_data/CatQuotes/CatQuotesCSV.csv']
    cat_quotes = []
    for f in cat_quote_files:
        cat_quotes.extend(Ingestor.parse(f))

    my_quote_files = ['./_data/MyQuotes/MyQuotesDOCX.docx',
                      './_data/MyQuotes/MyQuotesCSV.csv']
    my_quotes = []
    for f in my_quote_files:
        my_quotes.extend(Ingestor.parse(f))

    cat_res = AIEngine.detect_labels(s3_img, bucket, 'Cat')
    if (s3_img in cat_bucket) and cat_res:
        quote = random.choice(cat_quotes)
    dog_res = AIEngine.detect_labels(s3_img, bucket, 'Dog')
    if (s3_img in dog_bucket) and dog_res:
        quote = random.choice(dog_quotes)
    if s3_img in view_bucket:
        quote = random.choice(my_quotes)

    path = meme.make_meme(img, quote.body, quote.author)

    return path

if __name__ == "__main__":
    meme = MemeGenerator('./static')
    quotes, imgs = setup()
    path = meme_rand(quotes, imgs)
    #print(type(meme))
    #output = meme.make_meme('./_data/photos/picked/neymar_1.jpg', 'Hi there', 'Jonathan')
    email = Email('memegenerator886@gmail.com', 'BeautifulMeme2021')
    print(email.send('johnnyyeh0723@gmail.com', 'Send email with image test', 'Hi there', path))
