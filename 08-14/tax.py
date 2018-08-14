price = input("Enter a price: ")
price = float(price)

# now, price is a floating point number

price_plus_tax = price * 1.0775

print("The total with tax is", round(price_plus_tax, 2))
