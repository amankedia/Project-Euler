def isPalindrome(x):
    reverse = 0
    j = x
    while(j>0):
        reverse = reverse*10 + int(j%10)
        j = int(j/10)
    return reverse==x

def LargestPalindrome():
    max = 0
    for i in range(100,1000):
        for j in range(100, 1000):
           prod =  i*j
           if(prod>max and isPalindrome(prod)):
               max = prod
    return max

print(LargestPalindrome())
