def isWordGuessed(secretWord, lettersGuessed):
    '''
    secretWord: string, the word the user is guessing
    lettersGuessed: list, what letters have been guessed so far
    returns: boolean, True if all the letters of secretWord are in lettersGuessed;
      False otherwise
    '''
    if lettersGuessed == []:
        return False

    count = 0
    for l in lettersGuessed:
        if l in secretWord: 
            count += 1

    if count == len(secretWord): 
        return True
    else:
        return False            