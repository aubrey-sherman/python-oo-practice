from random import choice as pick_a_word


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    """

    def __init__(self, file_path):
        """ Will create an object representing the file to be read and a
            count property for the number of words read
        """
        self.formatted_word_list = self.read_and_format(file_path)
        self.words_read_count = self.count_words_read(self.formatted_word_list)

    def read_and_format(self, file_path):
        """take in a file path (aboslute or relative) and will
            return an object representing the file
        """
        word_list = open(f"{file_path}", "r").readlines()
        formatted_list = [item.strip() for item in word_list]

        return formatted_list

    def count_words_read(self, word_list):
        """take in a file object, will print the number of the words read
        """
        words_count = len(word_list)
        print(f"{words_count} words read")

    def random(self):
        """Given a list of words, will return a random word"""
        list_of_words = self.formatted_word_list
        random_word = pick_a_word(list_of_words)
        return random_word


class SpecialWordFinder(WordFinder):
    """Special Word Finder: find a random word in a document with special
        characters
    """

    # def __init__(self, file_path): NOTES: we don't need this, because this will look at parent's init
    #     """ Will create an object representing the file to be read and a
    #         count property for the number of words read
    #     """
    #     super().__init__(file_path)
    #     # print(self.formatted_word_list)

    def read_and_format(self, file_path):  # NOTES: the init will look at this on self
        child_read_and_format = super().read_and_format(file_path)  # raw word list
        return [item for item in child_read_and_format
                if item != "" and item[0] != "#"
                ]
