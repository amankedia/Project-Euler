def PythagoreanTriplet():
    flag=False
    prod = 0
    for a in range(1, 999):
        for b in range(2, 1000):
            for c in range(3, 1000):
                if((a+b+c)==1000 and ((a*a+b*b)==c*c)):
                    prod = a*b*c
                    flag=True
                    break
            if flag==True:
                break
        if flag == True:
            break
    return prod
print(PythagoreanTriplet())
