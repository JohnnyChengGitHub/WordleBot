
import file_reader

def get_pattern_from_guess(guess: str, hidden_word: str) -> str:

    
    pattern = green_letters(guess, hidden_word)
    return black_letters(guess, hidden_word,pattern) 




    
    

    


   
    """
    Given a guess and a hidden word, this function
    should output a hint. The hint in this case is
    a 5 letter string, where each letter is either
    'G', 'Y', or 'B'

    e.g. given the guess 'hello' for hidden word 'whale'
    the return value should be 'YYBGB'
    """



##Green 



    
          



def green_letters(guess,hidden_word):
    
    greenresult = ["X","X","X","X","X"]
    guess = list(guess)
    hidden_word = list(hidden_word)

    for x in range(len(guess)):  
        if guess[x] == hidden_word[x]:
            greenresult[x] = "G"
        
    return greenresult

## Black


def black_letters(guess,hidden_word, black):
    
    
    guess = list(guess)
    hidden_word = list(hidden_word)

    for x in range(len(guess)):  
        if guess[x] != hidden_word[x]:
            black[x] = "B"
        
    return "".join(black)

## Yellow Not Done

def yellow_letters(guess,hidden_word, yellow):
    
    
    guess = list(guess)
    hidden_word = list(hidden_word)

    for x in range(len(guess)):  
        if guess[x] != hidden_word[x]:
            black[x] = "B"
        
    return "".join(black)




      






            
            


