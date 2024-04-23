def read_file(file_path):
    """take in a file path (aboslute or relative) and will
        return an object representing the file
    """

    file_to_be_read = open(f"{file_path}", "r")
    return file_to_be_read


def count_words_read(file):
    """take in a file object, will print the number of the words read
    """
    words_count = len(file.readlines())
    print(f"{words_count} words read")


class WordFinder:
    """Word Finder: finds random words from a dictionary.
    """

    def __init__(self, file_path):
        """ Will create an object representing the file to be read and a
            count property for the number of words read
        """
        self.file_object = read_file(file_path)
        # double check it to pass in file_path as param
        self.words_read_count = count_words_read(self.file_object)

    def random(list_of_words):
        """Given a list of words, will return a random word"""
