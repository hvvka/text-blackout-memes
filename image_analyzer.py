import pytesseract
from pytesseract import Output
from PIL import Image, ImageDraw, ImageFilter
import os
import json
from util import utils
from rectangle import Rectangle

if os.path.isfile('resources/config.json'):
    with open(os.path.join(os.path.dirname(__file__), 'resources/config.json')) as json_file:
        data = json.load(json_file)
        pytesseract.pytesseract.tesseract_cmd = data['pytesseractPath']


def includes_word(data, word):
    data_iterator = -1
    word_counter = 0
    indices = []
    for char in word:
        while data_iterator < len(data) - 1:
            data_iterator += 1
            if char == data[data_iterator][0]:
                word_counter += 1
                indices.append(data[data_iterator])
                break

    if word_counter == len(word):
        return True, indices
    return False, []


def get_slangs_matches(slangs, image_boxes):
    result = []
    for slang in slangs:
        test = includes_word(image_boxes, slang.strip().lower().replace(" ", ""))
        if test[0]:
            result.append((slang, test[1]))
    return result


def get_boxes_from_image(image_path):
    d, n_boxes = get_boxes(image_path)
    result = []
    for i in range(n_boxes):
        (text, x1, y2, x2, y1) = (d['char'][i], d['left'][i], d['top'][i], d['right'][i], d['bottom'][i])
        result.append((d['char'][i], d['left'][i], d['top'][i], d['right'][i], d['bottom'][i]))
    return result


def get_difference_with(rectangle, visible_rectangles):
    processed_rectangle = Rectangle(int(rectangle[0]), int(rectangle[3]), int(rectangle[2]), int(rectangle[1]))
    difference_rects = []
    for visible_rect in visible_rectangles:
        b = Rectangle(int(visible_rect[1]), int(visible_rect[4]), int(visible_rect[3]), int(visible_rect[2]))
        difference_rects.extend(list(processed_rectangle - b))
    return set(difference_rects)


# XD dont even read this
def show_crossed_image(word, image_path, fill_color):
    original_image = Image.open(image_path)
    all_boxes, n_boxes = get_boxes(image_path)
    all_boxes_set = {(all_boxes['char'][i], all_boxes['left'][i],
                      all_boxes['top'][i], all_boxes['right'][i],
                      all_boxes['bottom'][i]) for i in range(n_boxes)}
    marked_letters_set = set(word[1])
    width, height = original_image.size
    draw = ImageDraw.Draw(original_image)
    # print(marked_letters_set)
    for box in all_boxes_set:
        (x1, y2, x2, y1) = (box[1], box[2], box[3], box[4])
        if box not in marked_letters_set:
            difference = get_difference_with((box[1], box[2], box[3], box[4]), marked_letters_set)
            # print(difference)
            if len(difference) > 1:
                # print('overlapped:', box)
                for diff_rect in difference:
                    # draw.rectangle([(diff_rect.x1, height - diff_rect.y1), (diff_rect.x2, height - diff_rect.y2)], outline = "#00FF00")
                    draw.rectangle([(diff_rect.x1, height - diff_rect.y1), (diff_rect.x2, height - diff_rect.y2)],
                                   fill=fill_color)
            else:
                for diff_rect in difference:
                    draw.rectangle([(diff_rect.x1, height - diff_rect.y1), (diff_rect.x2, height - diff_rect.y2)],
                                   fill=fill_color)
            # for diff_rect in difference:
            #     draw.rectangle([(diff_rect.x1, height - diff_rect.y1), (diff_rect.x2, height - diff_rect.y2)], fill = fill_color)
    # else:
    # print('found:', box[0])
    # draw.rectangle([(x1, height - y1), (x2, height - y2)], outline = "#FF0000")

    return original_image


def get_boxes(image_path):
    img = Image.open(image_path)
    img = img.convert('L')  # grayscale
    img = img.filter(ImageFilter.MedianFilter())  # a little blur
    img = img.point(lambda x: 0 if x < 140 else 255)  # threshold (binarize)
    all_boxes = pytesseract.image_to_boxes(img, output_type=Output.DICT)
    n_boxes = len(all_boxes['char'])
    return all_boxes, n_boxes


if __name__ == '__main__':
    all_slangs = utils.read_array('./resources/slangs.txt')
    image_path = "./memes/metzen.png"
    matches = get_slangs_matches(all_slangs, get_boxes_from_image(image_path))
    # print(matches[1:5])
    # utils.save_array(matches[1:5], 'mentzen_matches.txt')
    for match in matches:
        image = show_crossed_image(match, image_path, '#16202C')
        image.save(f"./mentzen/mentzen_{match[0]}.png")
