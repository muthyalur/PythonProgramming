import random


def guessInput():
    while(True):
        try:
            value = int(raw_input('Guess a number from 0 to %d: '%highest))
            return value
        except Exception as e:
            print 'Invalid input! The input should be in the range of 0 to %d'%highest

if __name__ == '__main__':
    highest = 10
    answer = random.randrange(highest)
    guess = -1
    while (guess != answer):
        guess = guessInput()
        if(guess < answer):
            print 'Answer is higher..'
        elif(guess > answer):
            print 'Answer is lower'
    raw_input('You\'re a winner face!!!')
