def gcdIter(a, b):
    '''
    a, b: positive integers
    
    returns: a positive integer, the greatest common divisor of a & b.
    '''
    first = a
    second = b
    if b <= a:
        while True:
            if b % second == 0 and a % second == 0:
                return second
            else:
                second -= 1
    else:
        while True:
            if a % first == 0 and b % first == 0:
                return first
            else:
                first -= 1
    
print str(gcdIter(17, 12))