balance = 4213
annualInterestRate = 0.2
monthlyPaymentRate = 0.04
monthlyInterestRate = annualInterestRate/12.00
totalMonth = 12
currentMonth = 1

minimum = 0
totalPaid = 0

while currentMonth <= totalMonth:
    print 'Month: ' + str(currentMonth)
    
    #calculate minimum monthly payment
    minimum = round(monthlyPaymentRate * balance, 2)
    print 'Minimum monthly payment: ' + str(minimum)
    
    #calculate remaining balance
    monthlyUnpaidBalance = round(balance - minimum, 2)
    balance = round(monthlyUnpaidBalance + (monthlyInterestRate * monthlyUnpaidBalance), 2)
    print 'Remaining balance: ' + str(balance)
    
    totalPaid = round(totalPaid + minimum, 2)
    currentMonth += 1

#print out totals
print '\nTotal paid: ' + str(totalPaid)
print 'Remaining balance: ' + str(balance)    
    
    