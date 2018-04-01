def nextPermu(arr):
    i = len(arr)-1
    while i>0 and arr[i-1] >= arr[i]:
        i = i-1
    if i<=0:
        return false
    j = len(arr) - 1
    while arr[i-1] >= arr[j]:
        j = j-1
    temp = arr[i-1]
    arr[i-1] = arr[j]
    arr[j] = temp
    j = len(arr) - 1
    while (i < j):
        temp = arr[i]
        arr[i] = arr[j]
        arr[j] = temp
        i = i + 1
        j = j - 1
    return arr
def main():
    arr = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    for i in range(0, 999999):
        arr = nextPermu(arr)
        #print(arr)
    permu = ""
    for i in range(0, len(arr)):
        permu = permu + str(arr[i])
    print(permu)
if __name__=="__main__":
    main()
