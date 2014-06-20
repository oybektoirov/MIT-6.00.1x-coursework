import string
def getAvailableLetters(lettersGuessed):
    '''
    lettersGuessed: list, what letters have been guessed so far
    returns: string, comprised of letters that represents what letters have not
      yet been guessed.
    '''
    availableLetters = ''
    allLetters = string.ascii_lowercase
    lettersList = []
    
    #load all letters into list
    for a in allLetters:
        lettersList.append(a)
        
    #remove a letter from lettersList if it's guessed
    for l in lettersGuessed:
        if l in lettersList:
            lettersList.remove(l)
            
    #load list to string
    for l in lettersList:
        availableLetters += l
            
    return availableLetters
