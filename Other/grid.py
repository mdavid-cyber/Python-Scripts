grid_width = int(input("Enter grid's width: "))
grid_height = int(input("Enter grid's height: "))

for row in range(grid_height):
    for col in range(grid_width):
        print("*", end="")
    print()


