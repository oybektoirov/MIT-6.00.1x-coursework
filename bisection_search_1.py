balance = 320000
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12

def newBalance(mainBal, middle):
    for month in range(12):
        mainBal -= middle
        mainBal *= (1 + monthlyInterestRate)
    return mainBal
 
lower = balance / 12
upper = (balance * ((1 + monthlyInterestRate) ** 12)) / 12
middle = 0.5 * (upper + lower)
mainBal = newBalance(balance, middle)
while abs(mainBal) > 0.000001:
    if mainBal < 0:
        upper = middle
    else:
        lower = middle
    middle = 0.5 * (upper + lower)
    mainBal = newBalance(balance, middle)
print "Lowest payment: " + str(round(middle, 2))
    
    



