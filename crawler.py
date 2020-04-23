from tqdm import tqdm
import requests
from lxml import html
import utils

def crawl_slangs():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    allSlangs = []
    for letter in tqdm(alphabet):
        pageNumber = 0
        page = requests.get(f'https://www.miejski.pl/{letter}-{pageNumber}.html')

        while page.status_code == 200:
            slangs = html.fromstring(page.content).xpath('//ul[@id="simple-link-list"]/li/a/text()')
            allSlangs.extend(slangs)
            pageNumber += 1
            page = requests.get(f'https://www.miejski.pl/{letter}-{pageNumber}.html')

    return allSlangs

if __name__ == '__main__':
    allSlangs = crawl_slangs()
    utils.save_array(allSlangs, 'slangs.txt')

