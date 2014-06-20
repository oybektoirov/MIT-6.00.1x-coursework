import random
print 'Please think of a number between 0 and 100!'

secret = random.randint(0, 100)
print 'Is your secret number ' + str(secret) + '?'

x = str(raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly: '))

while x != 'c':
    if x == 'h':
        secret = random.randint(0, secret)
    elif x == 'l':
        secret = random.randint(secret, 100)
    else:
        print "I could not understand your input."
    print 'Is your secret number ' + str(secret) + '?'
    x = str(raw_input('Enter "h" to indicate the guess is too high. Enter "l" to indicate the guess is too low. Enter "c" to indicate I guessed correctly: '))

print 'Game Over. Your secret number was: ' + str(secret)