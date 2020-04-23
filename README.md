# cross-out-memes

Find out what are possibilities to create meme 
by crossing-out letters from text on image.

| Not funny             |  Funny |
:-------------------------:|:-------------------------:
![boring](./memes/original.jpg) |  ![haha](./memes/funny.jpg)

[slangs.txt](./slangs.txt) contains **sample phrases** web-crawled from [polish slang dictionary](https://www.miejski.pl)
used to check their presence in ordered input string provided to [python script](./find_words.py).

## Python library requirements
```
pip install tqdm
pip install Pillow
pip install requests
pip install pytesseract
```

## Pytesseract installation

1. Download `tesseract` from: https://github.com/UB-Mannheim/tesseract/wiki

2. Create `config.json` file in main folder with content presented in [config.example.json](./config.example.json) file

3. Specify path to `tesseract` executable installed in step 1
