def apply_discount(original, discount=0):
    """"calculate discount"""
    discount_amount = original - discount
    return discount_amount

# case 1: no discount
original = 100
print(f"Original price: £{original}")
print(f"Discounted price: £{apply_discount(original)}\n")

# case 2: discount applied
discount = 15
print(f"Original price: £{original}")
print(f"Discount: £{discount}")
print(f"Discounted price: £{apply_discount(original, discount)}")
