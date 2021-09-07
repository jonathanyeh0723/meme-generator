"""Import libraries."""
import random
import os
import requests
from flask import Flask, render_template, abort, request

from QuoteEngine import Ingestor, QuoteModel
from MemeEngine import MemeGenerator
from AIEngine import AIEngine
from email_function import Email
import subprocess

app = Flask(__name__)

meme = MemeGenerator('./static')


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


quotes, imgs = setup()


@app.route('/')
def meme_rand():
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

    return render_template('meme.html', path=path)


@app.route('/create', methods=['GET'])
def meme_form():
    """User input for meme information."""
    return render_template('meme_form.html')


@app.route('/create', methods=['POST'])
def meme_post():
    """Create a user defined meme."""
    img_url = request.form['image_url']
    img_tmp = f'./tmp/{random.randint(0, 100000000)}.jpg'
    img_content = requests.get(img_url, stream=True).content
    with open(img_tmp, 'wb') as f:
        f.write(img_content)

    if request.method == 'POST':
        body = request.form.get('body')
        author = request.form.get('author')

    path = meme.make_meme(img_tmp, body, author)
    os.remove(img_tmp)

    return render_template('meme.html', path=path)


@app.route('/email', methods=['Get'])
def email_form():
    """User input for sending image email."""
    return render_template('email_form.html')


@app.route('/email', methods=['POST'])
def email_post():
    """Send email using generated meme."""
    if request.method == 'POST':
        s_email_addr = request.form.get('s_email_addr')
        s_email_passwd = request.form.get('s_email_passwd')
        r_email_addr = request.form.get('r_email_addr')
        r_email_subj = request.form.get('r_email_subj')
        r_email_body = request.form.get('r_email_body')

    email = Email(s_email_addr, s_email_passwd)

    #img = random.choice(imgs)
    #path = meme.make_meme(img, 'Hello World', 'Jonathan')
    #path = './static/' + os.listdir('./static')[-1]
    subprocess.call(["ls -lt ./static > images.txt"], shell=True)
    with open('images.txt', 'r') as f:
        for line in f:
            if line.startswith('-'):
                last_img = line.split(' ')[-1].strip('\n')
                break
    path = path = './static/' + str(last_img)
    email.send(r_email_addr, r_email_subj, r_email_body, path)

    return render_template('meme.html', path=path)


if __name__ == "__main__":
    app.run()
