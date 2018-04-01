def main():
    f = open("p022_names.txt", "r")
    f1 = f.readlines()
    text = f1[0].split(",")
    text.sort()
    totalSum = 0
    for i in range(0, len(text)):
        ithSum = 0
        text[i] = eval(text[i])
        #print("text[i]", text[i])
        for j in text[i]:
            ithSum = ithSum + ord(j)-64
        #print("ithSum", ithSum)
        totalSum = totalSum + (i+1) * ithSum
        #print("totalSum", totalSum)
    print(totalSum)
if __name__ == "__main__":
    main()
