def sum_odd(num):
    count = sum = 0
    for i in range(1,2*num,2):
        if i % 2 != 0:
            sum += i
            count += 1
    print(f"sum of the first {num} odd numbers is {sum}")
    
sum_odd(4)