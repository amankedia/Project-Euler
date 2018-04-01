import numpy as np
def numberOfDivisors():
    counter = 0
    i = 1
    number = 0
    #print(i)
    while(eachNumbersDivisor(number)<500):
        number = number + i
        i = i + 1
    #print("no", number)
    return number
def eachNumbersDivisor(number):
    count = 0
    sqrt = int(np.sqrt(number))
    #print("sqrt", sqrt, "number", number)
    for i in range(1, sqrt):
        if number % i == 0:
            count = count + 2
    if sqrt*sqrt == number:
        count = count - 1
    #print("count", count)
    return count
if __name__ == "__main__":
	counter = numberOfDivisors()
	print("counter", counter)
