def calculate_simpleinterest(principle,rate,time):
    simple_interest = (principle * rate * time)/ 100
    print(f"the simple interest if the principle is {principle},the rate is {rate}, the time is {time} is {simple_interest:.2f}")
    
    
calculate_simpleinterest(1000,5,10)