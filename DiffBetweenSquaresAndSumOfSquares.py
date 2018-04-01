def difference():
    squaresum = 0
    sum = 0
    for i in range(1, 101):
        squaresum = squaresum + i*i
        sum = sum + i
    sum = sum*sum
    return sum-squaresum
print(difference())
