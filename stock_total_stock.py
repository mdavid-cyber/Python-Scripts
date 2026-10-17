# store inventory with validation

# get details
name = input("Enter product name: ")
id = input("Enter product id: ")
price = float(input("Enter product price: "))
quantity = int(input("Enter product stock quantity: "))

stock_add = input("Do you want to add stock?:")

while stock_add == "yes":
    valid = True
    name = input("Enter product name: ")
    id = input("Enter product id: ")
    price = float(input("Enter product price: "))
    quantity = int(input("Enter product stock quantity: "))

    if price < 0:
        print("Price cannot be negative")
        valid = False

    if quantity < 0:
        print("Quantity cannot be negative")
        valid = False

        # calculate stock value
    if valid:
        stock_value = price * quantity

        # print stock value
        print(f"Product: {name}, ID: {id}, Price: £{price:.2f}, Quantity: {quantity}, Stock value: £{stock_value:.2f}")

        if quantity < 5:
            print("Low stock")

    stock_add = input("Do you want to add more stock?:")



