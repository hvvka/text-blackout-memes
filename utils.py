def save_array(array, fileName):
    with open(fileName, 'w', encoding="utf-8") as filehandle:
        for listitem in array:
            filehandle.write('%s\n' % listitem)

def read_array(fileName):
    array = []
    with open(fileName, 'r', encoding="utf-8") as filehandle:
        for line in filehandle:
            currentPlace = line[:-1]
            array.append(currentPlace)
    return array