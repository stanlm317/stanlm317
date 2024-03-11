message = input("Enter message here: ")
print(message)

# Ask if the user would like a drink
wantdrink = input("Would you like a drink? (y/n) ")
while wantdrink.lower() != "y" and wantdrink.lower() != "n":
    wantdrink = input("Invalid input. If you would like a drink, enter 'y'. Otherwise, enter 'n'. ")
if wantdrink.lower() == "y":
    drink = input("What would you like to drink? ")
    print(f"One {drink}, coming right up!")
else:
    print("Very well. Have a nice day!")
