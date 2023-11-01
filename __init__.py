def add(num_1, num_2):
    result = num_1 + num_2
    return result

def game():
    score = 0
    while True:
        print('======== Menu ========')
        print('1. Add')
        print('0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter the first number: '))
        num_2 = int(input('Enter the second number: '))
        answer = int(input('Enter your answer: '))
        if option == 1:
            result = add(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    print('======== Game Over ========'
        f'Your score is {score}'
        'Keep going!')

game()