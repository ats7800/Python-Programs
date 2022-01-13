friends = ['ashutosh', 'singh', 213, 's', False, True]
friends[1:4] = [4, "RajVeer", 1]
# print(friends[1:4])

# () repesents noneditable tuples
newList = ['vibha', (3, 1), 'usha']
friends.extend(newList)
friends.append('aditya')
friends.insert(2, "VishwaRaj")
print(friends)
print(friends.count(True))
friends.remove(True)
friends.remove(True)
print(friends)
print(friends.pop())
print(friends)
print(friends.index('usha'))
# friends.sort()
# print(friends)
numbers = [54, 24, 25, 64, 4, 2, 1221]
numbers.sort()
numbers.reverse()
fr = friends.copy()
print(numbers)
