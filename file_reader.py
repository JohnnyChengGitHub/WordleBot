from typing import List

def _load_word_file(path) -> List[str]:
    # initialize a list
    words: List[str] = []

    # open a file (aka ur wordle list) in read mode
    with open(path, "r") as f:
        # read the file line by line, and append each line to the list
        for line in f:
            words.append(line.strip().lower())
    return words

def load_hidden_words() -> List[str]:
    return _load_word_file("wordle_data/hidden_words.txt")

def load_word_bank():
    return _load_word_file("wordle_data/word_bank.txt")
