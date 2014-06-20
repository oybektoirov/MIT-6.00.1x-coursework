animals = { 'a': ['aardvark'], 'b': ['baboon'], 'c': ['coati']}

animals['d'] = ['donkey']
animals['d'].append('dog')
animals['d'].append('dingo')

def biggest(aDict):
    '''
    aDict: A dictionary, where all the values are lists.

    returns: The key with the largest number of values associated with it
    '''
    if aDict == '': return None
    num = 0
    biggest = 0
    key = ''
    for i in aDict:
        num = len(aDict[i])
        if num != '' and num > biggest:
            biggest = num
            key = i
    return key
print biggest(animals)