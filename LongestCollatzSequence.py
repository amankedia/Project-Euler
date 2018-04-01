def main():
    val = -1
    max = 0
    for i in range(1, 1000000):
        count = 0
        n = i
        while n > 1:
            count = count + 1
            #print(n)
            if n%2 == 0:
                n = n/2
            else:
                n = 3*n + 1
            if n <= 1:
                break
        if count>max:
            max = count
            val = i
            print("Max:", max, "Val:", val)
    return val        
if __name__ == "__main__":
	num = main()
	print(num)
