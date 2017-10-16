import argparse
import collections
import sys


def load_data(filepath):
    with open(filepath) as source_file:
        raw_data = [(line.strip()).split(' ') for line in source_file]
    return raw_data


def data_prepare(raw_data):
    words_list = [item for element in raw_data for item in element ]
    return words_list


def get_most_frequent_words(words_list):
    most_popular_words = 10
    for pair in collections.Counter(words_list).most_common(most_popular_words):
        #print(pair[0], pair[1])
        print('The word \'{}\' meets {} time(s)'.format(pair[0],pair[1]))


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('filepath', help='Path to file')
    args = parser.parse_args()
    filepath = args.filepath
    get_most_frequent_words(data_prepare(load_data(filepath)))
