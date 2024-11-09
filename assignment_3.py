""" 1. Create a function named calculate_discount(price, discount_percent) that calculates the final price after applying a discount. The function should take the original price (price) and the discount percentage (discount_percent) as parameters. If the discount is 20% or higher, apply the discount; otherwise, return the original price.
 """
def calculate_discount(price, discount_price):
    if (discount_price >= 20):
        final_price = price - (price * (discount_price/100))
        return final_price
    else :
        return price
    

calculate = calculate_discount(20, 30)
    
print(calculate) 
 
 
""" 2. Using the calculate_discount function, prompt the user to enter the original price of an item and the discount percentage. Print the final price after applying the discount, or if no discount was applied, print the original price. """

def calculate_discount(price, discount_price):
    if (discount_price >= 20):
        final_price = price - (price * (discount_price/100))
        return final_price
    else :
        return price

price_of_item = int(input("Enter the price for the item: "))
discount_for_item = int(input("Enter the discount percentage price for the item: "))

calculate = calculate_discount(price_of_item, discount_for_item)
    
print(f'The final price is {calculate}')