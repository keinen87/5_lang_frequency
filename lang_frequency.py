import collections
import os
import sys


def load_data(filepath):
    collections_counter = collections.Counter()
    if not os.path.exists(filepath):
        return None
    with open(filepath) as source_file:
        for line in source_file:
            for word in (line.rstrip()).split(' '):
                collections_counter[word] +=1
    return collections_counter

def get_most_frequent_words(words_dict):
    for pair in words_dict.most_common(10):
        print('Слово ' + '\'' + pair[0] + '\'',
              ' встречается ' + str(pair[1]) + ' раз(а)')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        get_most_frequent_words(load_data(filepath))
    else:
        print("Error! Enter path!")
