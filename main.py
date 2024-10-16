#if statements
#if, do something only IF a condition is True
#else do something else
#age = int(input("Enter your age: "))

#if age >=100:
#    print("You will die by heart attack if you watch these videos...")
#elif age >= 18:
#    print("Your are now signed up!")
#elif age < 0:
#    print("You haven't been born yet!")
#else:
#    print("You are under 18, dont subscribe to this site!")

#response = input("Would you like hoes? (Y or N): ")
#
#if response == "Y":
#    print("Have some hoes!")
#else:
#    print("No hoes for you!")

#name = input("Enter your name: ")
#
#if name == "":
#    print("You arent anonymous! Type your fkn name")
#else:
#    print(f"Thanks {name}")

#you can use if statements with conditions or boolean values
#onTrip = False
#
#if onTrip:
#    print("you're cooked")
#else:
#    print("you're sober, congrats!")

#Exercise - Calc
#
# num1 = float(input("Enter a number: "))
# op = input("Enter a operator: ")
# num2 = float(input("Enter a number: "))
#
# if op == "+":
#     res = num1 + num2
#     print(f"Result is {round(res, 2)}")
# elif op == "-":
#     res = num1 - num2
#     print(f"Result is {round(res, 2)}")
# elif op == "/":
#     res = num1 / num2
#     print(f"Result is {round(res, 2)}")
# elif op == "*":
#     res = num1 * num2
#     print(f"Result is {round(res, 2)}")
# else:
#     print("Invalid operator.")

#Exercise - Weight Converter
# print("Sis weight converter")
# weight = float(input("Enter your sis weight: "))
# unit = input("(1)-Kg or (2)-Pounds? ")

# if unit == "1":
#     weight = weight * 2.205
#     unit = "Lbs"
#     print(f"Your sis weights {round(weight, 1)} {unit}. ITS A WALE!")
# elif unit == "2":
#     weight = weight / 2.205
#     unit = "Kgs"
#     print(f"Your sis weights {round(weight, 1)} {unit}. ITS A WALE!")
# else:
#     print("Type a valid option your dumb ass")

#Exercise - Temperature Converter
# unit = input("Whats the unit measure (F or C)? ")
# temp = float(input("Enter the temperature: "))

# if unit == "F":
#     temp = ((temp - 32) * 5 / 9)
#     unit = "°C"
#     print(f"Temp is {round(temp, 1)} {unit}. Isnt hotter than your mom.")

# elif unit == "C":
#     temp = ((9* temp) / 5 + 32)
#     unit = "°F"
#     print(f"Temp is {round(temp, 1)} {unit}. Its colder than your ass.")

# else:
#     print("Type a valid measure unit, loser!")


#Logical operators
