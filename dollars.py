price = float(input("Enter the item price: $"))
money_given = float(input("Enter the dollars given: $"))

if money_given < price:
    print(f"Not enough money. You need ${price - money_given:.2f} more.")
else:
    change = money_given - price
    print(f"Give the customer back: ${change:.2f}")