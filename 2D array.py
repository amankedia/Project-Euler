# your code goes here
#dx = [0, 1]
#dy = [1, 0]

def main():
    matrix = []
    n = int(input())
    for i in range(0,n):
        matrix.append(list(map(int, input().split())))
    for i in range(0,n):
        for j in range(0,n):
            print(matrix[i][j])
if __name__ == "__main__":
	main()
