def drawline1():
    """drawing line characters 1"""
    character = "-"
    length = 10
    for _ in range(length):
        print(character, end="")
    print()

drawline1()

def drawline2():
    """drawing line characters 2"""
    character = "_"
    length = 10
    line = character * length
    return line

print(drawline2())

def drawline3():
    """drawing line characters 3"""
    character = input("Please put in character to be drawn: ")
    length = int(input("And what length would that be?: "))
    line = character * length
    return line

print(drawline3())

def drawline4(length = 0):
    """drawing line characters 4"""
    character = input("Please put in character to be drawn: ")
    choice = input("Do you want to add repetitions?: ")
    if choice == "yes":
        desired_length = int(input("And what length would that be?: "))
        return character * desired_length
    else:
        desired_length = 10
        return character * desired_length

print(drawline4())
