def add(num_1, num_2):
    result = num_1 + num_2
    return result

def subtract(num_1, num_2):
    result = num_1 - num_2
    return result

def multiply(num_1, num_2):
    result = num_1 * num_2
    return result

def game():
    score = 0
    while True:
        print('======== Menu ========')
        print('1. Add')
        print('2. Subtract')
        print('3. Multiply')  # Agregamos la opción de multiplicación
        print('0. Exit')
        option = int(input('\nChoose an option: '))
        if option == 0:
            break
        num_1 = int(input('Enter the first number: '))
        num_2 = int(input('Enter the second number: '))
        answer = int(input('Enter your answer: '))
        if option == 1:
            result = add(num_1, num_2)
        elif option == 2:
            result = subtract(num_1, num_2)
        elif option == 3:  # Si se elige la opción 3, utilizamos la función de multiplicación
            result = multiply(num_1, num_2)
        if result == answer:
            score += 1
            print('Correct!!')
        else:
            print('Incorrect')
    print('======== Game Over ========')
    print(f'Your score is {score}')
    print('Keep going!')

game()