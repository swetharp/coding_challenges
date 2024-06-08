def sumofnterms(n,arr):
    sum = 0
    for i in range(n):
        sum += arr[i]
    print(f"sum of first {n} terms in the series is {sum}")
    
sumofnterms(4,[3,7,11,15,19,23])