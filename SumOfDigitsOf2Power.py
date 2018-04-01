def main():
    num = 2**1000
    print(num)
    rem = 0
    while(num>0):
        print(rem)
        rem = rem + num%10
        num = int(num/10)
    return rem
if __name__=="__main__":
    num = main()
    print(num)
        
