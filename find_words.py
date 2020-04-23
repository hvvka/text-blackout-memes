import crawler
import utils

def includes_word(input, word):
    letter_index = []
    current_letter = 0

    for i, e in enumerate(input):
        if input[i] == word[current_letter]:
            current_letter += 1
            letter_index.append((i, input[i]))
            if current_letter >= len(word):
                break

    is_word_present = current_letter == len(word)
    if is_word_present:
        return word, letter_index


if __name__ == '__main__':
    input_string = "wałpzwpowodzoadinisttojewódzkizarządmelioracjiiurządzeńwodnywroc" \
            "ławulmatejki5aazrozkopywaniawbijanisszkadzaadarninyiinnychnpodstaapaez "
    # includes_word(input, "walewiadro")

    lines = utils.read_array('slangs.txt')

    output_file = open("output.txt", "w+")
    for line in lines:
        output = includes_word(input_string, line.strip().lower().replace(" ", ""))
        if output:
            word, indices = output
            output_file.write(word + " " + str(indices) + "\n")
    
    #START CRAWLING AGAIN
    #allSlangs = crawler.crawl_slangs()
    #utils.save_array(allSlangs, 'slangs.txt')
