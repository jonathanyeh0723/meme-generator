#!/bin/bash
# test for default values
echo "Test MemeEngine with defaults."
python3 meme.py

# test with arguments added
echo "Test MemeEngine with arguments added."
python3 meme.py -b '"Hello Udacity!"' -a 'Jonathan' -p "./_data/photos/picked/xander_4.jpg"
