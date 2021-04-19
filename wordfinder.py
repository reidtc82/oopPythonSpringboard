"""Word Finder: finds random words from a dictionary."""
import random
import os
import sys

class WordFinder:
    def __init__(self, file_location: str):
        self.f = open(file_location, "r")
        self.word_list = self.__get_words(self.f)

    def random(self) -> str:
        return self.word_list[random.randint(0, len(self.word_list))]

    def __get_words(self, f) -> [str]:
        result_list = []
        for l in f:
            result_list.append(l.strip('\n'))
        
        print("{0} words read".format(len(result_list)))
        return result_list


if __name__ == "__main__":
    gen = WordFinder(os.path.join(os.getcwd(), "words.txt"))
    print(gen.random())