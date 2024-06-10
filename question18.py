def days_to_month(days):
    #1 year = 365days, 1 month = 30days
    year = days // 365 
    remaining_days = days - year * 365 
    months = remaining_days // 30
    rest_days = remaining_days % 30
    print(f"the number of years is {year} ,the number of months is {months} and the remaining days is equal to {rest_days}")

days_to_month(400)
    
    
    
        
    