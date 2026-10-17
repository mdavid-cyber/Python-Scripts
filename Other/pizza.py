print("Our cheese and tomato pizza costs $8.00:")
pizza_cost = float(8.00)

mushrooms = float(1.00)
bacon = float(1.50)
pepperoni = float(1.50)
meatballs = float(2.00)

toppings = input ("would you like to add topings?: ")

if toppings == "yes":
    choice = input("please pick a choice from mushrooms, bacon, pepperoni, or meatballs toppings: ")

    if choice == "mushrooms":
        print("Thanks, total would be", pizza_cost + mushrooms)
    elif choice == "bacon":
        print("Thanks, total would be", pizza_cost + bacon)
    elif choice == "pepperoni":
        print("Thanks, total would be", pizza_cost + pepperoni)
    elif choice == "meatballs":
        print("Thanks, total would be", pizza_cost + meatballs)
    elif choice == "all":
        print(f"Thanks, total would be", pizza_cost + mushrooms + bacon + pepperoni + meatballs)
    else:
        print("We don't seem to have that option")
else:
    print(f"Total is :  {pizza_cost}")


