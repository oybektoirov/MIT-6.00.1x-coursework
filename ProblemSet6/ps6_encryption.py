# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "/Users/oybektoirov/Downloads/code_ProblemSet6/words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShift(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("/Users/oybektoirov/Downloads/code_ProblemSet6/story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    ### TODO.
    coder = {}
    pool = []
    shiftUpCase = shift
    secondShiftUpCase = 0
    shiftLowCase = 26 + shift
    secondShiftLowCase = 26
    
    for letter in string.ascii_uppercase:
        pool.append(letter)
    for letter in string.ascii_lowercase:
        pool.append(letter)
    for n in range(len(pool)):
        #for uppercase letters
        if (shiftUpCase + 1) <= 26 and n < 26:
            coder[pool[n]] = pool[shiftUpCase]
            shiftUpCase += 1
        elif (shiftUpCase + 1) >= 26 and n < 26:
            coder[pool[n]] = pool[secondShiftUpCase]
            secondShiftUpCase += 1
        
        #for lowercase letters
        elif (shiftLowCase + 1) <= (26 * 2) and n >= 26:
            coder[pool[n]] = pool[shiftLowCase]
            shiftLowCase += 1
        else:
            coder[pool[n]] = pool[secondShiftLowCase]
            secondShiftLowCase += 1
            
    return coder

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    ### TODO.
    codedTxt = ''
    for n in range(len(text)):
        if text[n] in coder:
            codedTxt += coder[text[n]]
        else:
            codedTxt += text[n]
    
    return codedTxt

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    real = 0
    maxReal = 0
    bestShift = 0
    codedTxt = ''
    splitTxt = []
    for n in range(26):
        codedTxt = applyShift(text, n)
        splitTxt = codedTxt.split(' ')
        for l in range(len(splitTxt)):
            if isWord(wordList, splitTxt[l]):
                real += 1
        if real > maxReal:
            maxReal = real
            bestShift = n
            
    return bestShift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    story = getStoryString()
    wordL = loadWords()
    bestShift = findBestShift(wordL, story)
    return applyShift(story, bestShift)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    wordList = loadWords()
    s = applyShift('Hello, world!', 8)
    bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    #    decryptStory()

print decryptStory()