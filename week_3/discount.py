def calculate_discount(price, discount):
    if discount >= 20:
        discount_price = price - (price * discount / 100)
        return discount_price
    else:
        return price
    
price = float(input("Enter the original price: "))
discount_percent = float(input("Enter the discount percentage: "))

final_price = calculate_discount(price, discount_percent)

print(f"The final price is: {final_price}")