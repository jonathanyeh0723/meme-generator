# Meme-Generator

[![Build Status](https://travis-ci.org/python/pythondotorg.svg?branch=main)](https://travis-ci.org/python/pythondotorg)
[![Documentation Status](https://readthedocs.org/projects/pythondotorg/badge/?version=latest)](https://pythondotorg.readthedocs.io/?badge=latest)
[![Apache License Version 2.0](https://img.shields.io/badge/license-Apache_2.0-green.svg)](LICENSE)

The meme generator lets you create memes with established quotes and images; moreover, you can customize your own beautiful memes and share them with your friends or loved ones!

![demo](./meme_generator_demo.gif)

## Overview
The meme generator is a multimedia application to dynamically generate memes, including an image with an overlaid quote. This packaged applications can be accessed in 2 ways. Command-line or web service. Not only we can generate random memes by command-line utility, but also we can interact with web interface, where you can generate random memes at the click of a button, or make your app accept user input through a post request.

![overview](./1_overview.jpg)

Below is a created meme demo inspired by one of my favorite movie, La La Land.

![lalaland](./lalaland.png)

## Block Diagram
This [overengineering](https://en.wikipedia.org/wiki/Overengineering) solution consists of 4 main modules – Quote Engine, Meme Engine, Plot Engine, and AI Engine.

![block_diagram](./2_block_diagram.jpg)

 - **Quote Engine**: The `Quote Engine` module is responsible for ingesting many types of files that contain quotes. For the sake of image maker with text purposes, a *quote* contains a *body* and an *author*.

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
- `IngestorInterface.py`: The ingestor interface backbone. It is a abstract base class work as a parent class for DocxImporter.py, CSVImporter.py, TXTImporter.py, PDFImporter.py, Ingestor.py.



## Setting up the environment

