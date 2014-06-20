import isWordGuessed
import getGuessedWord
import getAvailableLetters
secretWord = 'cheers'
def hangman(secretWord):
    lettersGuessed = []
    guesses = 8
    print('Welcome to the game Hangman!')
    print('I am thinking of a word that is ' + str(len(secretWord)) + ' letters long')
    while guesses > 0:
        print('-----------')
        if isWordGuessed.isWordGuessed(secretWord, lettersGuessed):
            print('Congratualtions! You won!')
        print('You have ' + str(guesses) + ' guesses left')
        print('Available letters: ' + getAvailableLetters.getAvailableLetters(lettersGuessed))
        guess = raw_input('Please guess a letter: ')
        guess = guess.lower()
        if guess in secretWord:
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Good guess: ' + getGuessedWord.getGuessedWord(secretWord, lettersGuessed))
            else:
                print("Oops! You've already guessed that letter: " + getGuessedWord.getGuessedWord(secretWord, lettersGuessed))        
        else:
            if guess not in lettersGuessed:
                lettersGuessed.append(guess)
                print('Oops! That letter is not in my word: ' + getGuessedWord.getGuessedWord(secretWord, lettersGuessed))
                guesses -= 1
            else:
                print("Oops! You've already guessed that letter: " + getGuessedWord.getGuessedWord(secretWord, lettersGuessed)) 
            
    print('-----------')
    if isWordGuessed.isWordGuessed(secretWord, lettersGuessed):
        print('Congratualtions, you won!')
    else:
        print('Sorry, you ran out of guesses. The word was ' + secretWord + '.')        
   

hangman(secretWord)        