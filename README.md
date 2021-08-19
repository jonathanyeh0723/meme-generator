# Meme-Generator

[![Build Status](https://travis-ci.org/python/pythondotorg.svg?branch=main)](https://travis-ci.org/python/pythondotorg)
[![Documentation Status](https://readthedocs.org/projects/pythondotorg/badge/?version=latest)](https://pythondotorg.readthedocs.io/?badge=latest)
[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)

The meme generator lets you create memes with established quotes and images; moreover, you can customize your own beautiful memes and share them with your friends or loved ones!

![demo](./my_meme_generator_demo.gif)

## Overview
The meme generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote. This packaged applications can be accessed in 2 ways. Command-line or web service. Not only we can generate random memes by command-line utility, but also we can interact with web interface, where you can generate random memes at the click of a button, or make your app accept user input through a post request.

![overview](./1_overview.jpg)

Below is a created meme demo inspired by one of my favorite movie, La La Land.

![lalaland](./lalaland.png)

## Block Diagram
This [overengineering](https://en.wikipedia.org/wiki/Overengineering) solution consists of 4 main modules – Quote Engine, Meme Engine, Plot Engine, and AI Engine.

![block_diagram](./2_block_diagram.jpg)

 - **Quote Engine**: The `Quote Engine` module is responsible for ingesting many types of files that contain quotes. For the sake of image maker with text, a *quote* contains a *body* and an *author*.
 - **Meme Engine**: The `Meme Engine` is responsible for manipulating and drawing text onto images. The object-oriented thinking is applied to demonstrate knowledge of using more advanced third party library for image manipulation.
 - **Plot Engine**: The `Plot Engine` module is responsible for data visualization for all the images contained in this program.
 - **AI Engine**:
 - **Meme App**
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
The meme engine module is used for image manipulation. The purpose is to generate image with resized width and height, and put text onto it.

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
Plot Engine is an individually special module. We can perform data visualization through this module to view all images included in this application. It will help us to have an overall picture of the photos used to generate random meme. In addition, we can check each image path based on AWS S3 printed on plotted figure as well.

### Structure of Plot Engine
```
.
├── __init__.py
├── PlotEngine.py
└── __pycache__
    ├── __init__.cpython-38.pyc
    └── PlotEngine.cpython-38.pyc

1 directory, 4 files
```

## Setting up the environment

### Build

### Test

### Deploy

## Pipeline

## Resources

