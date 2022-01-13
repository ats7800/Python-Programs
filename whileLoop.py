num = 524
steps = 0
while num!=1:
    steps+=1
    print(int(num))
    if num%2==0:
        num/=2
    else:
        num=(num*3)+1

print(str(int(num))+"\n")
print(steps)

