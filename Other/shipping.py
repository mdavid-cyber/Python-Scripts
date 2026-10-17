print("Welcome to super postings")

name = input ("What is your name? ")

parcel_shipment = input(f"And {name}, how would you like your parcel shipment today - Domestic or International?: ")

standard1 = 5.99
express1 = 7.99
standard2 = 10.99
express2 = 14.99

if parcel_shipment == "Domestic":
    delivery = input("Would you like standard or express shipping: ")
    if delivery == "standard":
        print(f"The cost for your standard shipment would be ${standard1}")
    elif delivery == "express":
        print(f"The cost for your express shipment would be ${express1}")
    else:
        print("Unfortunately, we can't process your package due to unrecognised shipment")

elif parcel_shipment == "International":
    delivery = input("Would you like standard or express shipping: ")
    if delivery == "standard":
        print(f"The cost for your standard shipment would be ${standard2}")
    elif delivery == "express":
        print(f"The cost for your express shipment would be ${express2}")
    else:
        print("Unfortunately, we can't process your package due to unrecognised shipment")

else:
    print("Unrecognised parcel shipment")
