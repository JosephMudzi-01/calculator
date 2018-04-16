def Welcome():
    print('''Welcome to Calculator''')
Welcome()

#Defining our function for calcultor
def calculate():
    operation = input(''' 
Please type in the math operatiom you would like to complete:
+ for addition
- for subtraction
* for multiplication
/ for division 
''')

#Take input from user
    number_1 = int(input('Please enter first number: '))
    number_2 = int(input('Please enter second number: '))

#Addition
    if operation == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2 )

#Subtraction
    elif operation == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

#Multiplication
    elif operation == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

#Division
    elif operation == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('You have not typed a valid operator , please run the program again')

#The again function triggers the code that asks the user whether or not thy would like to continue
    again()

def again():
    calc_again = input('''
Do you want to calculate again ?
Please type Y for YES or N for NO.
''')

    if calc_again.upper() == 'Y':
        calculate()

    elif calc_again.upper() == 'N':
        print('thank you ,see you again')

    else:
        again()

calculate()