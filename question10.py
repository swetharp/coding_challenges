def sumofneven(n):
    sum = count = 0
    for i in range(2,2*n+2,2):
        if i %2 ==0:
            sum +=i
    print("sum of first n even numbers is ",sum)

sumofneven(4)  