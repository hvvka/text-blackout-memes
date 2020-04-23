# cross-out-memes

Find out what are possibilities to create meme 
by crossing-out letters from text on image.

| Not funny             |  Funny |
:-------------------------:|:-------------------------:
![boring](./memes/original.jpg) |  ![haha](./memes/funny.jpg)

[slangs.txt](./slangs.txt) contains **sample phrases** web-crawled from [polish slang dictionary](https://www.miejski.pl)
used to check their presence in ordered input string provided to [python script](./find_words.py).

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
    
- Create `config.json` file in main folder with content presented in [config.example.json](./config.example.json) file
- Download EXE [here](https://github.com/UB-Mannheim/tesseract/wiki)
- Specify path to `tesseract` executable installed in [config.json](./config.json)
