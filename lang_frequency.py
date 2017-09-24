import os
import sys


frequent_words_list = ['и', 'в', 'не', 'на', 'я', 'быть', 'он', 'с', 'что',
                       'по', 'это', 'она', 'этот', 'к', 'но', 'они', 'мы',
                       'как', 'из', 'у', 'который', 'то', 'за', 'свой', 'что',
                       'весь', 'год', 'от', 'так', 'о', 'для', 'ты', 'же',
                       'все', 'тот', 'мочь', 'вы', 'человек', 'такой', 'его',
                       'сказать', 'только', 'или', 'ещё', 'бы', 'себя', 'один',
                       'как', 'уже', 'до', 'время', 'если', 'сам', 'когда',
                       'другой', 'вот', 'говорить', 'наш', 'мой', 'знать',
                       'стать', 'при', 'чтобы', 'дело', 'жизнь', 'кто',
                       'первый', 'очень', 'два', 'день', 'её', 'новый', 'рука',
                       'даже', 'во', 'со', 'раз', 'где', 'там', 'под', 'можно',
                       'ну', 'какой', 'после', 'их', 'работа', 'без', 'самый',
                       'потом', 'надо', 'хотеть', 'ли', 'слово', 'идти',
                       'большой', 'должен', 'место', 'иметь', 'ничто',  'а'
                       ]

result_dict = {i: 0 for i in frequent_words_list}


def load_data(filepath):
    if not os.path.exists(filepath):
        return None
    with open(filepath) as source_file:
        for line in source_file:
            for word in (line.rstrip()).split(' '):
                for i in range(len(frequent_words_list)):
                    if frequent_words_list[i] == word:
                        result_dict[frequent_words_list[i]] += 1
    return result_dict


def get_most_frequent_words(words_dict):
    for pair in sorted(words_dict.items(), key=lambda x: x[1], reverse=True)[:10]:
        print('Слово ' + '\'' + pair[0] + '\'',
              ' встречается ' + str(pair[1]) + 'раз')


if __name__ == '__main__':
    if len(sys.argv) > 1:
        filepath = sys.argv[1]
        get_most_frequent_words(load_data(filepath))
    else:
        print("Error! Enter path!")
