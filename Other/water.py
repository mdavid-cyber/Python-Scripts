name_company = input("Please put in your company's name: ")
Company_id = input("Please put in your company's ID: ")
Registered_Temperature = float(input("Designated Temperature in celsius: "))

if Registered_Temperature >= 100:
    print("gas")
elif 1 <= Registered_Temperature <= 99:
    print("Liquid")
else:
    print("solid")

