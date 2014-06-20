def oddTuples(aTup):
    '''
    aTup: a tuple
    
    returns: tuple, every other element of aTup. 
    '''
    i = 0
    c = 0
    bTup = ()
    while i < len(aTup):
        x = aTup[c]
        bTup += (x,)
        c += 2
        i += 2
    return bTup

tup = ('I', 'am', 'a', 'test', 'tuple')
print oddTuples(tup)