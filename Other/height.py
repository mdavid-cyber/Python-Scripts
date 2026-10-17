def height_in_inches(feet, inches):
    """results of the heights in inches"""
    total_inches = (feet * 12) + inches
    return total_inches

feet = int(input("Enter feet: "))
inches = int(input("Enter your inches: "))

heights = height_in_inches(feet, inches)
print(f"your height in inches is {heights} inches")
      
