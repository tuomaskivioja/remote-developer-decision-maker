potions = {
    "Invisibility Potion": ["Moonstone", "Dragon scale", "Fairy dust"],
    "Flying Potion": ["Phoenix feather", "Troll tooth", "Mermaid scale"],
    "Healing Potion": ["Unicorn horn", "Elf hair", "Golden apple"]
}

# Displaying the list of potions using a for loop
print("Welcome to the Magic Potion Shop!")
print("Here are the potions we offer:")
for potion in potions:
    print(potion)

# Taking user input
chosen_potion = input("Which potion would you like to buy ingredients for? ")

if chosen_potion in potions:
    print(f"\nThe ingredients for {chosen_potion} are:")
    for ingredient in potions[chosen_potion]:
        print(ingredient)

    print("\nLet's start buying the ingredients!")
    i = 0
    while i < len(potions[chosen_potion]):
        buy = input(f"Do you want to buy {potions[chosen_potion][i]}? (yes/no) ")
        if buy.lower() == "yes":
            print(f"You bought {potions[chosen_potion][i]}!")
            i += 1
        elif buy.lower() == "no":
            print("You chose to stop shopping.")
            break
        else:
            print("Invalid input. Please answer with 'yes' or 'no'.")

    if i == len(potions[chosen_potion]):
        print(f"\nCongratulations! You bought all the ingredients for {chosen_potion}!")
else:
    print("That potion is not available!")

