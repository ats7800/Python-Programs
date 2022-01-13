import time
number = 1_000

maxSteps = 1
maxStepNum = 1

timeStart = time.perf_counter()
while number > 0:
    num = number
    steps = 0
    while num != 1 :
        steps += 1
        if num % 2 == 0:
            num /= 2
        else:
            num = (num * 3) + 1
    if maxSteps <= steps:
        maxSteps=steps
        maxStepNum=number
    number -= 1

timeEnd = time.perf_counter()

print(f"Time taken: {timeEnd-timeStart}")
print("Steps: ", maxSteps)
print("Number ", maxStepNum)

