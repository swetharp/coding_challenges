def sum_of_series(n, arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    print("the sum of the numbers in the arr is",sum)
    
sum_of_series(4,[5,7,9,11,13])