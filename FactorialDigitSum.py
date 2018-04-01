def multiply(v, x):
    carry = 0
    size = len(v)
    #print("size", size)
    #print("x", x)
    #print("v begin", v)
    for i in range(0, size):
     #   print("i", i)
        res = carry + v[i]*x
        v[i] = res%10
        carry = int(res/10)
    #print(v)
    while carry!=0:
        v.append(carry%10)
        carry = int(carry/10)
    #print("Size of v", len(v))
    #print("V in multiply", v)
    return v

def main():
    v = []
    n = int(input())
    v.append(1)
    for i in range(1, n+1):
        v = multiply(v, i)
    sum = 0
    size = len(v)
    #print("Size here", size)
    #print(v)
    for i in range(0, size):
        sum = sum + v[i]
    return sum
if __name__=="__main__":
    print(main())
