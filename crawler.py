from tqdm import tqdm
import requests
from lxml import html
import utils


def crawl_slangs():
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    all_slangs = []
    for letter in tqdm(alphabet):
        page_number = 0
        page = requests.get(f'https://www.miejski.pl/{letter}-{page_number}.html')

        while page.status_code == 200:
            slangs = html.fromstring(page.content).xpath('//ul[@id="simple-link-list"]/li/a/text()')
            all_slangs.extend(slangs)
            page_number += 1
            page = requests.get(f'https://www.miejski.pl/{letter}-{page_number}.html')

    return all_slangs


if __name__ == '__main__':
    all_slangs = crawl_slangs()
    utils.save_array(all_slangs, 'resources/slangs.txt')
