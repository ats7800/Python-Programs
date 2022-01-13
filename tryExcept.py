inputSucces = False

while not inputSucces:
    try:
        number = int(input('Enter the Number:\n'))
        inputSucces = True
    except ValueError:
        print('Only enter Integers')
        print('Lets try again')
        inputSucces = False

print(number)

