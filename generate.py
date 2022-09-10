from train import dict_of_words

import random


def main():
    prefix = random.choice(list(dict_of_words.keys()))
    length = 30
    sentence = [prefix]
    for i in range(length):
        next = random.choices(list(dict_of_words[sentence[-1]].keys()), weights=list(dict_of_words[sentence[-1]].values()))
        sentence.append(next[0])
    print(' '.join(sentence))


if __name__ == '__main__':
    main()