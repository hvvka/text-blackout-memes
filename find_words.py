import crawler
import utils
import argparse
import logging

logging.basicConfig(level=logging.INFO)
LOG = logging.getLogger(__name__)


def includes_word(string, word):
    """
    Sample usage: includes_word(default_string, "walewiadro")
    """
    letter_index = []
    current_letter = 0

    for i, e in enumerate(string):
        if string[i] == word[current_letter]:
            current_letter += 1
            letter_index.append((i, string[i]))
            if current_letter >= len(word):
                break

    is_word_present = current_letter == len(word)
    if is_word_present:
        return word, letter_index


if __name__ == '__main__':
    default_string = "wałpzwpowodzoadinisttojewódzkizarządmelioracjiiurządzeńwodnywroc" \
                   "ławulmatejki5aazrozkopywaniawbijanisszkadzaadarninyiinnychnpodstaapaez"

    parser = argparse.ArgumentParser()
    parser.add_argument("--input", default=default_string, help="input string")
    parser.add_argument("--dict", default="slangs.txt", help="dictionary file path (optional)")
    parser.add_argument("--out", default="output.txt", help="output file path (optional)")
    args = parser.parse_args()

    cmd_line_args = list()
    cmd_line_args.append(args.input)
    cmd_line_args.append(args.dict)
    cmd_line_args.append(args.out)

    LOG.debug("Parsed args: %s", cmd_line_args)
    input_string, dictionary_path, output_path = cmd_line_args

    lines = utils.read_array(dictionary_path)

    output_file = open(output_path, "w+")
    for line in lines:
        output = includes_word(input_string, line.strip().lower().replace(" ", ""))
        if output:
            word, indices = output
            output_file.write(line.strip() + " " + str(indices) + "\n")

    #START CRAWLING AGAIN
    #allSlangs = crawler.crawl_slangs()
    #utils.save_array(allSlangs, 'slangs.txt')
