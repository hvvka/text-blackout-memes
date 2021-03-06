# text-blackout-memes

[![Build Status](https://travis-ci.com/hvvka/text-blackout-memes.svg?branch=master)](https://travis-ci.com/hvvka/text-blackout-memes)

Find out what are possibilities to create a meme 
by crossing-out letters from text on image.

A part of [text-blackout meme series](https://knowyourmeme.com/memes/text-blackout).

| Not funny             |  Funny |
:-------------------------:|:-------------------------:
![boring](./memes/original.jpg) |  ![haha](./memes/funny.jpg)

[slangs.txt](resources/slangs.txt) contains **sample phrases** web-crawled from [polish slang dictionary](https://www.miejski.pl)
used to check their presence in ordered input string provided to [python script](./find_words.py).

## Requirements

Python 3.X

```bash
$ python setup.py install
```

## Pytesseract installation

Install [tesseract](https://github.com/tesseract-ocr/tesseract/wiki)

tl;dr
    
Linux
```bash
$ sudo apt install tesseract-ocr
$ sudo apt install libtesseract-dev 
```
   
MacOS
```bash
$ brew install tesseract
```
    
Windows
    
- Create `config.json` file in main folder with content presented in [config.example.json](resources/config.example.json) file
- Download EXE [here](https://github.com/UB-Mannheim/tesseract/wiki)
- Specify path to `tesseract` executable installed in [config.json](resources/config.json)


## Using Docker

Image available at https://hub.docker.com/repository/docker/hvvka/text-blackout-memes

### Build locally

```bash
$ docker build -t memes_image .
$ docker run -it --name memes_container memes_image
```

## Usage notes

### [find_words](find_words.py)

Checks **input string** for a given **file with dictionary words** and outputs those which **are present in string + their positions**.

I.e. `default_string` in [find_words.py](find_words.py) for given [slangs.txt](resources/slangs.txt) outputs [output.txt](resources/output.txt).

3 arguments are possible, but optional:

- _--input_ – input string provided from image, default: `wałpzwpowodzoadinisttojewódzkizarządmelioracjiiurządzeńwodnywrocławulmatejki5aazrozkopywaniawbijanisszkadzaadarninyiinnychnpodstaapaez`

- _--dict_ – file with dictionary words, default: `resources/slangs.txt`

- _--out_ – output file, default: `resources/output.txt`

If dictionary file is not present, then it uses [polish_slang_crawler](util/polish_slang_crawler.py) script to fetch words.
The script can we modified to use different source.

Use output file to find the most suitable phrase and modify the image manually. 

### [image_analyzer](image_analyzer.py)

Manual image modification is not required with this one.

1. Run [image_anaylzer.py](image_analyzer.py) and wait for gigabytes of data with mentzen memes

