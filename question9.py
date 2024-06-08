def display_nthodd(num):
    count = 0
    for i in range(1,2*num,2):
        count+=1
        if count == num:
            print("the nth odd number is ",i )
            
display_nthodd(4)