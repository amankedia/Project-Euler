def prime():
    ctr = 0
    i=2
    while(ctr<10002):
        flag = True
        for j in range(i-1, 2, -1):
            if i % j == 0:
                flag = False
                break
        if flag == True:
            #print(i)
            ctr = ctr + 1
            print(ctr)
        if ctr == 10001:
            num = i
        i=i+1
    return num
print(prime())
