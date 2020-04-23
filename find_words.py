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
        print(letter_index)


if __name__ == '__main__':
    input = "wałpzwpowodzoadinisttojewódzkizarządmelioracjiiurządzeńwodnywroc" \
            "ławulmatejki5aazrozkopywaniawbijanisszkadzaadarninyiinnychnpodstaapaez "
    # includes_word(input, "walewiadro")

    fp = open('slangs.txt', 'r')
    lines = fp.readlines()

    for line in lines:
        includes_word(input, line.strip().lower())
