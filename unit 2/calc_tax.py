item = input("whats the item? ")
price = input("whats the price? ")
rate = .06875
rate = float(rate)
price = int(price)
calculate_tax = (item, price, rate)

tax = (price * rate)
total = (price + rate)

total = float(total)
item = str(item)
tax = float(tax)

def calculate_tax(item, price, rate):
    return (price * rate)

def calculate_tax(item, price, rate):
    tax = calculate_tax(item, price, rate)
    return (price + tax)

print(item +" costs " + str(price) + " dollars before tax and " + str(total) + " after tax.")

