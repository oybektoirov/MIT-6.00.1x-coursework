def lenIter(aStr):
    '''
    aStr: a string
    
    returns: int, the length of aStr
    '''
    count = 0
    for s in aStr:
        count += 1
    return count

print str(lenIter("word"))