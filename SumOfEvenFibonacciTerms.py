def FiboEvenSum(x):
    a = 1
    b = 2
    sum=b
    while(a+b<=4000000):
        c = a+b
        a=b
        b=c
        if(c%2==0):
            sum = sum+c
    return sum
print(FiboEvenSum(10))
