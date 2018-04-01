import math
def SumOfAllPrimes():
    sum = 2
    num = 3
    while(num<2000000):
        prime = True
        limit = int(math.sqrt(num))+1
        for i in range(2, limit):
            if (num%i) == 0:
                #print("num", num, "i", i)
                #print(num)
                prime = False
                break                
        if prime == True:
            #print(num)
            print(num)
            sum = sum + num
        num = num + 1
    return sum
print(SumOfAllPrimes())
