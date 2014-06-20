def recurPower(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float, base^exp
    '''
    # Base case is when exp = 0
    if exp <= 0:
        return 1

    # Otherwise, exp must be > 0, so return 
    #  base* base^(exp-1). This is the recursive case.
    return base * recurPower(base, exp - 1)

print str(recurPower(4, 3))

def recurPowerNew(base, exp):
    '''
    base: int or float.
    exp: int >= 0

    returns: int or float; base^exp
    '''
    if exp == 0:
        return 1
    elif exp > 0 and exp % 2 == 0:
        return (base * base)**(exp/2)
    elif exp > 0 and exp % 2 == 1:
        return base * recurPower(base, exp - 1)
print str(recurPowerNew(24, 3))