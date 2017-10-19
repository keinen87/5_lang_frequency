import argparse
import re
from collections import Counter


def get_words_list(filepath):
    with open(filepath, "r") as file_reader:
        file_data = file_reader.read()
    return file_data


def get_most_frequent_words(words_list):
    words_count = 10
    return Counter(re.findall(r'\w+', words_list)).most_common(words_count)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to file')
    args = parser.parse_args()
    filepath = args.filepath
    most_frequent_words = get_most_frequent_words(get_words_list(filepath))
    for i, pair in enumerate(most_frequent_words, 1):
        print('{} word \'{}\' meets {} time(s)'.format(i, pair[0], pair[1]))
