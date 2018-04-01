def check(x, y):
    if (x<0 or y<0 or x>=2 or y>=2):
        return False
    else:
        return True

def main():
    n = int(input())
    grid = []
    for i in range(0, n+1):
        new = []
        for j in range(0, n+1):
            new.append(0)
        grid.append(new)
    #grid[0][0]=1
    for i in range(0, n+1):
        grid[0][i]=1
        grid[i][0]=1
    for i in range(1, n+1):
        for j in range(1, n+1):
            grid[i][j] = grid[i-1][j] + grid[i][j-1]
    return grid[n][n]

if __name__ == "__main__":
	num = main()
	print(num)
