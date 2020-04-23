def save_array(array, file_name):
    with open(file_name, 'w', encoding="utf-8") as file_handler:
        for item in array:
            file_handler.write('%s\n' % item)


def read_array(file_name):
    array = []
    with open(file_name, 'r', encoding="utf-8") as file_handler:
        for line in file_handler:
            current_place = line[:-1]
            array.append(current_place)
    return array
