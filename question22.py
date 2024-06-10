def calspecofmarks(sub1,sub2,sub3,sub4,sub5):
    total = sub1 + sub2 + sub3 + sub4 + sub5
    avg = total / 5
    percentage = avg * 100
    print(f"the total marks is {total}, the average marks is {avg :.2f} and the percentage is {percentage}")


calspecofmarks(45,50,65,68,30)