def LargestPrimeFactor(x):
    #num = -1
    for i in range(2, int(x/2)):
        if x%i==0:
            #print(i)
            x = x/i
            #print("x", x)
            if x==1:
                num = i
                break
    return num
print(LargestPrimeFactor(600851475143))
