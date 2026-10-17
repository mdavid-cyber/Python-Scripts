my_friends = {}
Chole = {
    "age": 19,
    "partner": "dave",
    "children": ["Evelyn", "charlotte", "lindy"],
    "pets": {"dog":"oreo", "cat":"turbo"}
}
Ava = {
    "age": 20,
    "partner": "sam",
    "children": ["hazel", "sophie", "mia"],
}

options = ("add friends", "remove", "find", "list", "add kids", "add pets", "or end")
print(options)

actions = input("what would you like to do from options above?:").strip().lower()
print(actions)
while actions != "end":
    if actions == "add friend" or actions == "add":
        name = input("what's is the name?: ")

        if name in my_friends:
            print(f"name {name} already exists")
        else:
            age = int(input("what's is the age?: "))
            partner = input("Enter your partner if any: ")

            my_friends[name] = {
                "age": age,
                "partner": partner if partner else None,
                "children": [],
                "pets": {}
            }
            print(f"name {name} was added")

    elif actions == "find":
        name = input("what's the name of the friend you are looking for?: ")
        if name in my_friends:
            print(f"Here's the found result for {name}, {my_friends[name]}")
        else:
            print(f"{name}, could not be found in your friends list :(")

    elif actions == "remove":
        name = input("what's the name of the friend you are looking to remove?: ")
        if name in my_friends:
            del my_friends[name]
            print(f"name {name} was removed :)")
        else:
            print(f"name {name} is not in friends :(")

    elif actions == "list":
        if my_friends:
            for names, details in my_friends.items():
                print(names, ":", details)
        else:
            print("no friends in the list :(")

    elif actions == "add kids":
        name  = input("whose kids do you want to add: ")

        if name in my_friends:
            num = int(input("how many kids do you want to add?: "))
            for _ in range(num):
                kids = input("give name(s): ")
                if kids in my_friends[name]["children"]:
                    print(f"name {kids} already exists")
                else:
                    my_friends[name]["children"].append(kids)
        else:
            print(f"{name} does not exist in your friends list.")

    elif actions == "add pets":
        name = input("whose pets are you adding?: ")

        if name in my_friends:
            num = int(input("how many pets are you adding?: "))
            for _ in range(num):
                pet_specie = input("what's the specie of the pet?: ")
                pet_name = input("and what's the name of the pet?: ")
                if pet_name in my_friends[name]["pets"]:
                    print(f"{pet_name} already exists")
                else:
                    my_friends[name]["pets"][pet_name] = pet_specie
        else:
            print(f"{name} does not exist in your friends list.")

    else:
        print("Invalid action")

    actions = input("would you like to choose another options again?: ").strip().lower()

print("Thanks")























