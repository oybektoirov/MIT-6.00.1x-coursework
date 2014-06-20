balance = 4773
annualInterestRate = 0.2
monthlyInterestRate = annualInterestRate/12.0

minimum = 0
newBalance = balance
while newBalance > 0:
    newBalance = balance
    minimum += 10
    for month in range(12):
        newBalance -= minimum
        newBalance *= (1 + (monthlyInterestRate))
print "Lowest payment: " + str(minimum)

