def main():
    n = int(input())
    matrix = []
    for i in range(0, n+1):
        new = []
        for j in range(0, n+1):
            new.append(0)
        matrix.append(new)
    for i in range(0, n):
        f = list(map(int, input().split()))
        for j in range(0, i+1):
            #print(i, j)
            matrix[i][j] = f[j]
    for i in range(n-2, -1, -1):
        for j in range(0, i+1):
            #print(i, j)
            if matrix[i+1][j] > matrix[i+1][j+1]:
                matrix[i][j] = matrix[i][j] + matrix[i+1][j]
            else:
                matrix[i][j] = matrix[i][j] + matrix[i+1][j+1]
   # for i in range(0, n):
    #    for j in range(0, n):
     #       print(matrix[i][j])
    print(matrix[0][0])
if __name__ == "__main__":
    main()
