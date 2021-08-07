import random
def guess(x):
    random_number = random.randint(1, x)
    guess = 0
    while guess != random_number:
         guess_n = int(input(f'Guess A Number Between 1 And {x}: '))
         if guess_n < random_number:
             print('Too Low.')
         elif guess_n > random_number:
             print('Too High')
         elif guess_n == random_number:
              print(f'You have guess The number {random_number} correctly')
              exit()
def computer_guess(x):
    low = 1
    high = x
    feedback = ''
    while feedback != 'c':
        if low != high:
            guess = random.randint(low, high)
        else:
            guess = low #could also be high b/c low = high
        feedback = input(f'Is {guess} too high (H), too low (L), or correctly!!')
        if feedback == 'h':
           high = guess - 1
        elif feedback == 'l':
           low = guess + 1

    print(f'Yay! The Computer guessed your number, {guess}, correctly')
   
computer_guess(1000)