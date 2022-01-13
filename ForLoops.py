friends = ['AdityaLamboo', "AdityaAlien", 'Satpreet']
for eachFriend in friends:
    print(eachFriend.upper())

for index in range(len(friends)):
    print(friends[index])

for letter in friends[0]:
    print(letter.upper()," ")

goodNumber = 23184
digitSum = 0
for eachDigit in range(len(str(goodNumber))):
    digitSum += int(str(goodNumber)[eachDigit])
    print(digitSum)

print('\n')
print(digitSum)

numberGrid = [
    [2,3,4],
    [1,3,5],
    [2, 4]
]

for row in numberGrid:
    for elem in row:
        print(elem)

for rowNum in range(len(numberGrid)):
    for colNum in range(len(numberGrid[rowNum])):
        print(numberGrid[rowNum][colNum])

