import os
import random
import argparse

# @TODO Import your Ingestor and MemeEngine classes
from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator


def generate_meme(path=None, body=None, author=None):
    """ Generate a meme given an path and a quote """
    img = None
    quote = None

    if path is None:
        images = "./_data/photos/picked/"
        imgs = []
        for root, dirs, files in os.walk(images):
            imgs = [os.path.join(root, name) for name in files]

        img = random.choice(imgs)
    else:
    #    img = path[0]
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
    # @TODO Use ArgumentParser to parse the following CLI arguments
    # path - path to an image file
    # body - quote body to add to the image
    # author - quote author to add to the image
    parser = argparse.ArgumentParser(description="Using ArgumentParser to parse the path, body, and author for meme generation.")
    parser.add_argument("-p", "--path", type=str, default=None, help="the path to an image file")
    parser.add_argument("-b", "--body", type=str, default=None, help="the quote body to add to the image")
    parser.add_argument("-a", "--author", type=str, default=None, help="the quote author to add to the image")

    args = parser.parse_args()
    print(generate_meme(args.path, args.body, args.author))
