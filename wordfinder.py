"""Word Finder: finds random words from a dictionary."""
import random
import os
import sys


class WordFinder:
    def __init__(self, file_location: str):
        """Constructor for child class SpecialWordFinder. This one does validation.

        Args:
            file_location (str): Full path to file with list of words. One word per line.
        """
        self.f = open(file_location, "r")
        self.word_list = self.__get_words(self.f)

    def random(self) -> str:
        """Selects a random word from the list.

        Returns:
            str: The word it selected.
        """
        return self.word_list[random.randint(0, len(self.word_list) - 1)]

    def __get_words(self, f) -> [str]:
        """Private method to take an open file and read in lines to a list for
        random selection.

        Args:
            f (file): an open file. Could work with a list as well.

        Returns:
            [str]: A list of strings.
        """
        result_list = [l.strip() for l in f]

        print("{0} words read".format(len(result_list)))
        return result_list


class SpecialWordFinder(WordFinder):
    def __init__(self, file_location: str):
        """Constructor for child class SpecialWordFinder. This one does validation.

        Args:
            file_location (str): Full path to file with list of words. One word per line.
        """
        self.f = open(file_location, "r")
        self.word_list = self.__get_words(self.f)

    def __get_words(self, f) -> [str]:
        """Private method to take an open file and read in lines to a list for
        random selection. Performs some validation on each line read.

        Args:
            f (file): an open file. Could work with a list as well.

        Returns:
            [str]: A list of strings.
        """
        result_list = [l.strip() for l in f if l.strip() and not l.startswith("#")]

        print("{0} words read".format(len(result_list)))
        return result_list


if __name__ == "__main__":
    gen = SpecialWordFinder(os.path.join(os.getcwd(), "alt_words.txt"))
    print(gen.random())
