import pytesseract
from pytesseract import Output
from PIL import Image, ImageDraw
import os
import json

with open(os.path.join(os.path.dirname(__file__), 'config.json')) as json_file:
    data = json.load(json_file)
    pytesseract.pytesseract.tesseract_cmd = data['pytesseractPath']


def includes_word(data, word):
    data_iterator = -1
    word_counter = 0
    indexes = []
    for char in word:
        while data_iterator < len(data) - 1:
            data_iterator += 1
            if char == data[data_iterator][0]:
                word_counter += 1
                indexes.append(data[data_iterator])
                break

    if word_counter == len(word):
        return True, indexes
    return False, []


def get_slangs_matches(slangs, image_boxes):
    result = []
    for slang in slangs:
        test = includes_word(image_boxes, slang)
        if test[0]:
            result.append((slang, test[1]))
    return result


def get_boxes_from_image(file_name):
    d = pytesseract.image_to_boxes(file_name, output_type=Output.DICT)
    n_boxes = len(d['char'])
    result = []
    for i in range(n_boxes):
        (text, x1, y2, x2, y1) = (d['char'][i], d['left'][i], d['top'][i], d['right'][i], d['bottom'][i])
        result.append((d['char'][i], d['left'][i], d['top'][i], d['right'][i], d['bottom'][i]))
    return result


# THIS SHOULD BE GET CROSSED IMAGE AND USED IN A LOOP WITH ALL POSSIBLE MATCHES
def show_crossed_image(word, original_image, fill_color):
    all_boxes = pytesseract.image_to_boxes(original_image, output_type=Output.DICT)
    n_boxes = len(all_boxes['char'])
    all_boxes_set = {(all_boxes['char'][i], all_boxes['left'][i],
                      all_boxes['top'][i], all_boxes['right'][i],
                      all_boxes['bottom'][i]) for i in range(n_boxes)}
    marked_letters_set = set(word[1])
    width, height = original_image.size
    draw = ImageDraw.Draw(original_image)
    print(all_boxes_set)
    for box in all_boxes_set:
        (x1, y2, x2, y1) = (box[1], box[2], box[3], box[4])
        if box not in marked_letters_set:
            draw.rectangle([(x1, height - y1), (x2, height - y2)], fill=fill_color)
        else:
            draw.rectangle([(x1, height - y1), (x2, height - y2)], outline="#FF0000")
    original_image.show()


if __name__ == '__main__':
    all_slangs = ['lewak', 'heh', 'Zawias']
    image_path = r'.\memes\metzen.png'
    matches = get_slangs_matches(all_slangs, get_boxes_from_image(image_path))
    show_crossed_image(matches[0], Image.open(image_path), '#16202C')
