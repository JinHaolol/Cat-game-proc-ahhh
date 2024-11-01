cat_attributes = {
    "intelligence": 10,
    "energy": 10,
    "weight": 10
}

print("Welcome to Jin Hao's cat game!!")

#user inputs for the name and color of the cat
name = input("Enter the name of your cat: ")
color = input("Enter the color of your cat: ")

print(f"\nGreat! You've created a {color} cat named {name}!")

# start the while loop
while True:
    # Finish the string below
     print("\nWhat would you like to do?")
     print("1. Play with " + name)
     print("2. Train " + name)
     print("3. Feed " + name)
     print("4. Put " + name + " to sleep")
     print("5. View " + name + "'s stats")
     option = input("Choose an option (1-5): ")
    
      #options
     if option == '1':
        # Play with the cat
        cat_attributes["energy"] -= 10
        cat_attributes["weight"] -= 1
        print(f"\nYou played with {name}! Energy decreased by 10, weight decreased by 1.")

     elif option == '2':
        # Train the cat
        cat_attributes["intelligence"] += 2
        cat_attributes["energy"] -= 5
        print(f"\nYou trained {name}! Intelligence increased by 2, energy decreased by 5.")

     elif option == '3':
        # Feed the cat
        cat_attributes["weight"] += 2
        cat_attributes["energy"] += 5
        print(f"\nYou fed {name}! Weight increased by 2, energy increased by 5.")

     elif option == '4':
        # Put the cat to sleep
        cat_attributes["energy"] += 10
        print(f"\n{name} is sleeping... Energy increased by 10.")

     elif option == '5':
        # View cat's stats
        print(f"\n{name}'s stats:")
        for attribute, value in cat_attributes.items():
            print(f"{attribute.capitalize()}: {value}")
     else:
        print("\nOption not found, please try again.")

    # Check if any attribute is below a level
     if cat_attributes["energy"] <= 0:
        print(f"\n{name} is too tired!! Put {name} to sleep to regain energy. ;-;")
        cat_attributes["energy"] = 5  # Restore a minimum energy level
     elif cat_attributes["weight"] <= 0:
        print(f"\n{name} is underweight!! Feed {name} to regain weight. ;-;")
        cat_attributes["weight"] = 5  # Restore a minimum weight level
     elif cat_attributes["intelligence"] == 50: # Genius Cat
        print(f"\n{name} is now a genius! {name} now understands basic english. :P")
     elif cat_attributes["intelligence"] == 100: # Human IQ
        print(f"\n{name} is as intelligent as the average human now :P")
     elif cat_attributes["intelligence"] == 160: # Albert Einsinte IQ
        print(f"\n{name} is as smart as Albert Einstein!! :P ")                 
     elif cat_attributes["weight"] > 100: # Dead from obesity
        print(f"\n{name} died from overweight. Restart again!! X-X")
        break
     elif cat_attributes["weight"] <= 1: # Dead from underweight
        print(f"\n{name} died from being too light. Restart again!! X-X")
        break