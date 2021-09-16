# Meme-Generator

[![Build Status](https://travis-ci.org/python/pythondotorg.svg?branch=main)](https://travis-ci.org/python/pythondotorg)
[![Documentation Status](https://readthedocs.org/projects/pythondotorg/badge/?version=latest)](https://pythondotorg.readthedocs.io/?badge=latest)
[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)

The meme generator lets you create memes with established quotes and images; moreover, you can customize your own beautiful memes and share them with your friends or loved ones!

![demo](./my_meme_generator_demo.gif)

## Overview
The meme generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote. 

This packaged applications can be accessed in 2 ways: 
 - Command-Line
 - Web Service

Not only we can generate random memes by command-line utility, but also we can interact with web interface, where you can generate random memes at the click of a button, or make your app accept user input through a post request.

![overview](./1_overview.jpg)

Below is a created meme demo inspired by one of my favorite movie, La La Land.

![lalaland](./lalaland.png)

## Block Diagram
This [overengineering](https://en.wikipedia.org/wiki/Overengineering) solution consists of 4 main modules – Quote Engine, Meme Engine, Plot Engine, and AI Engine.

![block_diagram](./2_block_diagram.jpg)

 - **Quote Engine**: The `Quote Engine` module is responsible for ingesting many types of files that contain quotes. For the sake of image maker with text, a *quote* contains a *body* and an *author*.

 - **Meme Engine**: The `Meme Engine` is responsible for manipulating and drawing text onto images. The object-oriented thinking is applied to demonstrate knowledge of using more advanced third party library for image manipulation.

 - **Plot Engine**: The `Plot Engine` module is responsible for data visualization for all the images contained in this program.

 - **AI Engine**: The `AI Engine` is responsible for object detection. It leverage [Amazon Rekognition](https://aws.amazon.com/rekognition/?nc1=h_ls&blog-cards.sort-by=item.additionalFields.createdDate&blog-cards.sort-order=desc) to identify the image content and define rules to choose the quote category.

 - **Meme App**:
 - **Meme Generator**:

## QuoteEngine
This module will be composed of many classes. The complex inheritance, abstract classes, classmethods, strategy objects and other fundamental programming principles of Python are used to complete this module.

### Structure of Quote Engine
```
.
├── CSVImporter.py
├── DocxImporter.py
├── IngestorInterface.py
├── Ingestor.py
├── __init__.py
├── PDFImporter.py
├── QuoteModel.py
└── TXTImporter.py

0 directories, 8 files
```

- `__init__.py`: To make Python treat directories containing it as modules. Furthermore, this is the first file to be loaded in a module, so you can use it to execute code that you want to run each time a module is loaded, or specify the submodules to be exported.
- `QuoteModel.py`: Blueprint for quote.
- `IngestorInterface.py`: The ingestor interface backbone. It is a abstract base class works as a parent class for DocxImporter.py, CSVImporter.py, TXTImporter.py, PDFImporter.py, and Ingestor.py.
- `DocxImporter.py`: Child class of `IngestorInterface` to ingest 'docx' file extension.
- `CSVImporter.py`: Child class of `IngestorInterface` to ingest 'csv' file extension.
- `TXTImporter.py`: Child class of `IngestorInterface` to ingest 'txt' file extension.
- `PDFImporter.py`: Child class of `IngestorInterface` to ingest 'pdf' file extension.
- `Ingestor.py`: Child class of `IngestorInterface` to implement logic to select the appropriate helper for a given file based on filetype.

## Meme Engine
The meme engine module is used for image manipulation. The purpose is to generate image with resized width and height, and then put the quotes onto it.

### Structure of Meme Engine
```
.
├── fonts
│   ├── LilitaOne-Regular-1.ttf
│   └── LilitaOne-Regular-2.ttf
├── __init__.py
└── MemeGenerator.py

1 directory, 4 files
```

 - `__init__.py`: Special file that declares that a directory is a Python module. .
 - `MemeGenerator.py`: Define MemeGenerator class to manipulate image.
 - `fonts`: A directory contains 2 font templates.

## Plot Engine
Plot Engine is an individually special module. We can perform data visualization by using [matplotlib](https://matplotlib.org/) to view all images included in this application. It will help us to have an overall picture of the photos used to generate random meme. In addition, we can check each image path based on [Amazon S3 (Simple Storage Service)](https://aws.amazon.com/s3/) printed on plotted figure as well.

![matplotlib](./matplotlib.jpg)

### Structure of Plot Engine
```
.
├── __init__.py
└── PlotEngine.py

0 directories, 2 files
```
 - `__init__.py`: To let the Python interpreter know that a directory contains code for a Python module.
 - `PlotEngine.py`: Define PlotEngine class to conduct data visualization.

The following is a sample of using Plot Engine to execute data visualization for all dog photos.

![dog_photos](./xanders_photos.jpg)

## AI Engine
The core concept of AI Engine is to carry out image inference and detect labels. We define rules and use label extracted to let the computer automatically class the image with correspondent quotes. Basically, we utilize Amazon Rekognition for this task.

![aws_rek](./rek.jpg)

What is Amazon Rekognition?
 - Amazon Rekognition is a service that makes it easy to add powerful visual analysis to our applications. 
 - It is based on the highly scalable, deep learning technology developed by Amazon’s computer vision scientists to analyze billions of images and videos daily.
 - That way, it requires no machine learning expertise to use. We don’t need to handle complex AI infrastructure or deal with time-consuming model training.

In this case,

![detect_example](./detect_label_example.jpg)

### Structure of AI Engine
```
.
├── AIEngine.py
└── __init__.py

0 directories, 2 files
```
 - `__init__.py`: To define what gets brought into the namespace with the import statement.
 - `AIEngine.py`: Define AI Engine class to utilize AWS Rekognition to detect labels in the photo.

## Set up

 - OS: Linux distribution - [Ubuntu 20.04.3 LTS](https://ubuntu.com/download/desktop). We can check the [release notes](https://wiki.ubuntu.com/FocalFossa/ReleaseNotes?_ga=2.218895194.2117983555.1631591363-727216992.1631591363) to see an overview of the release and documentation of the known issues in detail.
 - Python version: [3.8.10](https://www.python.org/downloads/release/python-3810/)

**Prerequisites**: To install Python virtual environment establishment, package management system (pip), and some useful libraries.
```
$ sudo apt install -y python3.8-venv python3-pip python3-tk curl vim git
```

## Build, Test, Deploy

### Build
First, clone this repository to create a local copy on your computer.
```
$ git clone https://github.com/jonathanyeh0723/meme-generator
```

Next, create an isolated virtual environment for this project (in this example: meme-env).
```
$ python3 -m venv meme-env
```

Once the virtual environment was created, you can activate it.
```
$ source meme-env/bin/activate
```

After that, using following commands to install all the python packages are required to run this app.
```
$ pip install -r requirements.txt
```

Further, we need to configure basic settings that the AWS Command Line Interface (AWS CLI) uses to interact with AWS API.
The following example shows sample values. **Replace them with your own values** as described in the following sections.
```
$ aws configure
AWS Access Key ID [None]: AKIAIOSFODNN7EXAMPLE
AWS Secret Access Key [None]: wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY
Default region name [None]: us-west-2
Default output format [None]: json
```

### Test

We're all set! Now we can navigate to the src folder to start testing.
```
$ cd src/
```

### Test for QuoteEngine module
```
$ python3 QuoteEngine_test.py
```

We should be able to see the following output, if successful:
```
Test for DocxImporter:
[<"Bark like no one’s listening" ,  Rex>, <"RAWRGWAWGGR" ,  Chewy>, <"Life is like peanut butter: crunchy" ,  Peanut>, <"Channel your inner husky" ,  Tiny>]
Test for CSVImporter:
[<Chase the mailman, Skittle>, <When in doubt, go shoe-shopping, Mr. Paws>]
Test for TXTImporter:
[<﻿To bork or not to bork ,  Bork>, <He who smelt it... ,  Stinky>]
Test for PDFImporter:
[<"Treat yo self" ,  Fluffles>, <"Life is like a box of treats" ,  Forrest Pup>, <"It's the size of the fight in the dog" ,  Bark Twain>]
Test for Ingestor:
[<"Treat yo self" ,  Fluffles>, <"Life is like a box of treats" ,  Forrest Pup>, <"It's the size of the fight in the dog" ,  Bark Twain>]
Using ./_data/DogQuotes/DogQuotesPDF.pdf
```

### Test for MemeEngine module
```
$ sh MemeEngine_test.sh
```
We should be able to see something like below:
```
Test MemeEngine with defaults.
./tmp/299769.png
Test MemeEngine with arguments added.
./tmp/578978.png
```
In addition, we can verify the tmp directory to see the generated meme.
```
$ ls tmp/
299769.png  578978.png
```
Check out what we just created.
```
$ eog tmp/299769.png
```
![random_meme](299769.png)

```
$ eog tmp/578978.png
```
![random_meme](578978.png)

### Test for PlotEngine module
Run PlotEngine_test.py script with `--help` to see what argument needed to specify. 
```
$ python3 PlotEngine_test.py --help
usage: Parse a photo set to view data [-h] photo_set

positional arguments:
  photo_set   cat_photos, dog_photos, view_photos, all_photos

optional arguments:
  -h, --help  show this help message and exit
```
For instance, let’s have an overview for all the photos we have:
```
$ python3 PlotEngine_test.py 'all_photos'
Number of images: 12
Data visualization for images: ['xander_1.jpg', 'xander_2.jpg', 'xander_3.jpg', 'xander_4.jpg', 'neymar_1.jpg', 'neymar_2.jpg', 'neymar_3.jpeg', 'neymar_4.jpeg', 'iceland_1.jpeg', 'iceland_2.jpeg', 'iceland_3.jpeg', 'iceland_4.jpeg']
```
![all_photos](all_photos.png)

### Test for AIEngine module
Run AIEngine_test.py to see what argument needed to specify.
```
$ python3 AIEngine_test.py --help
usage: Parse image & label for AI recognition [-h] [-pt PRINT_LABELS] [-s SHOW] photo target

positional arguments:
  photo                 Dog: xander_1.jpg, xander_2.jpg, xander_3.jpg, xander_4.jpg; Cat: neymar_1.jpg, neymar_2.jpg, neymar_3.jpeg, neymar_4.jpeg; View: iceland_1.jpeg, iceland_2.jpeg,
                        iceland_3.jpeg, iceland_4.jpeg
  target                To specify target label to detect, Dog, Cat or view: Antler, Mountain, Nature, River, etc.

optional arguments:
  -h, --help            show this help message and exit
  -pt PRINT_LABELS, --print_labels PRINT_LABELS
                        To print labels detected from the image
  -s SHOW, --show SHOW  Show the bounding boxes for the labels detected
```

Let's grab a dog photo for the test. 
```
$ python3 AIEngine_test.py 'xander_2.jpg' 'Dog'
```
We should be able to see following reflected from the console, if successful:
```
[ Print Info ] To predict Dog label...

----------
Detected labels for xander_2.jpg

Label: Dog
Confidence: 99.11785125732422
Instances:
Bounding box
 Top: 0.02342822216451168
 Left: 0.006567688193172216
 Width: 0.9914323091506958
 Height: 0.9745717644691467
Confidence: 99.11785125732422

Parents:
   Pet
   Canine
   Animal
   Mammal
.
.
----------

[ Print Info ] Dog label detected: True
```

![ai_xander](AIEngine_test_xander.jpg)

Let's pick a cat photo for testing.
```
python3 AIEngine_test.py 'neymar_4.jpeg' 'Cat'
```

We should be able to see following reflected from the console, if successful:
```
[ Print Info ] To predict Cat label...

----------
Detected labels for neymar_4.jpeg

Label: Cat
Confidence: 90.30731964111328
Instances:
Bounding box
 Top: 0.5292110443115234
 Left: 0.6587520837783813
 Width: 0.25333595275878906
 Height: 0.3358360826969147
Confidence: 90.30731964111328

Parents:
   Pet
   Mammal
   Animal
----------
.
.
[ Print Info ] Cat label detected: True
```

![ai_neymar](AIEngine_test_neymar.jpg)

### Deploy

## Demo: Using meme generator with email function to send what you create to your friend or loved one!

![demo_with_email](pipeline_demo_email.gif)

## Resources

