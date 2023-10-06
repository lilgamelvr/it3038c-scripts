# idea and original version from
# https://www.digitalocean.com/community/tutorials/how-to-make-a-calculator-program-in-python-3

def calculator():
    options = input('''
    Please chose which math operator that you want to use for the equation
    If you want addition, enter +
    If you want subtraction, enter -
    If you want multiplication, enter *
    If you want division, enter /
    ''')  # this allows the user to enter an operator, and tells the user what the correct operators are,
    # and goes back if an invalid item is entered

    num1 = int(input('Enter your first number: '))  # the number that will be affected by the second number and operator
    num2 = int(input('Enter your second number: '))  # the number that will affect the first number

    if options == '+':
        print('{} + {} = '.format(num1, num2))  # prints the equation to console
        print(num1 + num2)  # adds the two numbers together and prints it to console
        another()  # calls another()
    elif options == '-':
        print('{} - {} = '.format(num1, num2))  # prints the equation to console
        print(num1 - num2)  # subtracts the first number by the second number and prints it to console
        another()  # calls another()
    elif options == '*':
        print('{} * {} = '.format(num1, num2))  # prints the equation to console
        print(num1 * num2)  # multiples the first number by the second number and prints it to console
        another()  # calls another()
    elif options == '/':
        print('{} / {} = '.format(num1, num2))  # prints the equation to console
        print(num1 / num2)  # divides the first number by the second number and prints it to console
        another()  # calls another()
    else:
        print(options + ' is not a valid operator, Please try again')  # the error when an invalid operator is entered
        calculator()  # Calls calculator()


def another():
    another_equation = input('''
    Equation successful, Would you like to do another equation (Y for yes, N for No):
    ''')  # Asks if you want to do another equation, and gives you a choice of Yes or No

    if another_equation.upper() == 'Y':
        calculator()  # Calls calculator()
    elif another_equation.upper() == 'N':
        print('Thanks for using the calculator, see you again soon')  # Ends program with message
    else:
        print(another_equation + ' was not a valid choice, Please try again') # Error for invalid choice
        another()  # Loops to the beginning by calling itself


calculator()  # Calls calculator()
