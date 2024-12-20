from random import randint

low_num, hig_num = 1, 10
random_number: int = randint(low_num, hig_num)
print(f'Guess the nuber in the range from {low_num} to {hig_num}.')

while True:
    try:
        user_guess: int = int(input('Guess: '))
    except ValueError as e:
        print('Plese, enter a valid number.')
        continue
    if user_guess > random_number:
        print('The number is lower.')
    elif user_guess < random_number:
        print('The number is higher')
    else: 
        print('You guessed it!')
        break 