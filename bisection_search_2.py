def isIn(char, aStr):
    '''
    char: a single character
    aStr: an alphabetized string
    
    returns: True if char is in aStr; False otherwise
    '''
    if aStr == '' or char == '': return False
    size = int(len(aStr)/2)
    if size == 1: size = 0
    if char == aStr[size:size + 1] or char == aStr[size:]: 
        return True
    elif char > aStr[size:size + 1] and char <= aStr[len(aStr) - 1]:
        return isIn(char, aStr[size + 1:])
    elif char < aStr[size:size + 1]:
        return isIn(char, aStr[0:size])
    else:
        return False
