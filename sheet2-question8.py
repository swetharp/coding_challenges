def calculate_final_price(price,GST):
    final_price = price + GST
    print(f"The final price when the price is {price} and GST is {GST} is {final_price}")
    
calculate_final_price(100,15)