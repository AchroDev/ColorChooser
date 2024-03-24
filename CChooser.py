print ("Your color choices are red, blue, green, white or yellow.")
#Prompts the user for input.
userColor = input("Enter a color from the list above: ")
print(userColor)

#Set the input value to all lowercase
color = userColor.lower()
print(color)

#Starts off a variable to run a check later and ensure the input data is a valid color
validColor = True
print(validColor)

#Translates the users choice to the color name in Spanish
if color == "red":
    spanishColor = "rojo"
elif color == "blue":
    spanishColor = "azule"
elif color == "green":
    spanishColor = "verde"
elif color == "white":
    spanishColor = "blanco"
elif color == "yellow":
    spanishColor = "amarillo"
else:
    validColor = False

#Checks if the users input is a valid choice from the list and writes the appropriate response.
if validColor:
    print("The color", color, "in Spanish is", spanishColor)
else:
    print("That is not a valid color, please choose a valid color from the list!")