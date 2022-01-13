def say_hi():
    print('hi')
    print('hi')


print('hello')
say_hi()
say_hi()


def processor(num):
    if num % 2 == 0 and num % 4 == 0 or num % 3 == 1:
        return num*num
    else:
        return num*num*num


print(processor(7))
is_tall = True
is_male = False


def tall_male():
    if is_male and is_tall:
        print('tall male')
    elif is_tall and not is_male:
        print('tall female')
    elif is_male and not is_tall:
        print('short male')
    else:
        print('short female')


tall_male()


def max_num(num1, num2, num3):
    if num1 > num2:
        if num1 > num3:
            return num1
        elif num3 > num1:
            return num3
    elif num2 > num3:
        return num2
    else:
        return num3


print(max_num(3, 9, 5))

