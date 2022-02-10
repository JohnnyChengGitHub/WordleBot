import file_reader

def get_pattern_from_guess(guess: str, hidden_word:str) -> str:
    pattern = ["X","X","X","X","X"] 
    green = (reveal_green(guess, hidden_word, pattern))
    black = (reveal_black(guess, hidden_word, green))
    yellow = (reveal_yellow(guess, hidden_word, black))
    return "". join(yellow)
    """
    Given a guess and a hidden word, this function
    should output a hint. The hint in this case is
    a 5 letter string, where each letter is either
    'G', 'Y', or 'B'

    e.g. given the guess 'hello' for hidden word 'whale'
    the return value should be 'YYBGB'
    """
def reveal_green(guess, hidden_word, pattern):
    for i in range(len(guess)):
        char_a = guess[i]
        char_b = hidden_word[i]
        if char_a == char_b:
            pattern[i] = "G"
    return pattern
def reveal_black (guess,hidden_word, pattern):
    for i in range(len(guess)):
        char_a = guess[i]
        char_b = hidden_word[i]
        if char_a != char_b:
            pattern[i] = "B"
    return pattern
def reveal_yellow(guess, hidden_word, pattern):
    for i in range(len(guess)):
        char_a = guess[i]
        for j in range (len(guess)):
            char_b = hidden_word[j]
            if (char_a == char_b and i != j):
                pattern [i] = "Y"
    return pattern


#     # return NotImplementedError
