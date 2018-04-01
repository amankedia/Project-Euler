import numpy as np
def sumDivisors(x):
    sum = 1
    j = x
    sqrt = int(np.sqrt(x))
    for i in range(2, sqrt):
        if j%i==0:
            #print(j, i, j/i)
            sum = sum + i
            sum = sum + (j/i)
    if sqrt*sqrt == x:
        sum = sum - sqrt
    #print(sum)
    return sum

def isAmicable(a, b):
    if sumDivisors(a) == b and sumDivisors(b) == a:
        return True
    else:
        return False
"""
def main():
    print(sumDivisors(8039))
    print(isAmicable(2,3))
"""
def main():
    sum = 0
    for i in range(1, 10000):
        for j in range(i+1, 10000):
            truth = isAmicable(i, j)
            if truth == True:
                print(i, j)
                sum = sum + i + j
    print(sum)

if __name__=="__main__":
    main()
