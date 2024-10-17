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


#Logical operators, evaluate multiple conditions (or, and, not)
##or - one of conditions must be true
# temp = 25
# is_raining = False

# if temp > 35 or temp < 15 or is_raining:
#     print("Your mom will not go out today.")
# else:
#     print("Lets get the pussy outside!")

##and - both conditions must be true
# temp = 25
# is_sunny = False

# if temp >= 25 and is_sunny:
#     print("Outside is HOT as your ass")
#     print("It is sunny!")
# elif temp <= 0 and is_sunny:
#     print("IT IS COLD COLD COLD COLD OUTSIDE")
#     print("It is sunny!")
# elif 28 > temp > 0 and is_sunny:
#     print("It is WAAARM outside")
#     print("It is sunny!")
##not - inverts the condition, not False or not True
# elif temp >= 25 and not is_sunny:
#     print("Outside is HOT as your ass")
#     print("It is cloudy!")
# elif temp <= 0 and is_sunny:
#     print("IT IS COLD COLD COLD COLD OUTSIDE")
#     print("It is cloudy!")
# elif 28 > temp > 0 and is_sunny:
#     print("It is WAAARM outside")
#     print("It is cloudy!")


#Conditional Expression - shortcut for if-else
#X IF condition ELSE y

#num = 5
#print("Positive" if num > 5 else "Negative")
#result = "Even" if num % 2 == 0 else "ODD"
#print(result)

#String Methods
#name = input("Enter your full name: ")
#len function - returns the num of characters on a string
# result = len(name)
# print(result)

#find - returns the first occurence of a character
#result = name.find ("B")
#print(result)

#rfind - returns the last occurence of a character
#result = name.rfind ("i")
#print(result)

#capitalize - capitalize first character
#name = name.capitalize()
#print(name)

#upper - uppercases all characters
#name = name.upper()
#print(name)

#lower - lwoercases all characters
#name = name.lower()
#print(name)

#isdigit - return true or false if string contains only digits
#result = name.isdigit()
#print(result)

#isalpha - return true or false if string contains only alphabetic characters
#result = name.isalpha()
#print(result)

#count - how many specific characters a string contains
# phone = input("Enter your phone number: ")
# result = phone.count("-")
# print(result)

#replace - replaces one character to another
# phone = input("Enter your phone number: ")
# phone = phone.replace("-", "")
# print(phone)

#print a detailed list of string methods
#print(help(str))

#Exercise - Validade user input exercise
#1- username is no more than 12 characters
#2- username must not contain spaces
#3- username must not contain digits

#method that I used
# username = input("Enter your name(12 character limit, without spaces and digits): ")
# username_lenght = len(username)
# username_alpha = username.isalpha()
# username_digit = username.isdigit()

# if username_lenght > 12 or username_alpha == False or username_digit == True:
#     print("Read again your bastard...")
# else:
#     print("Thanks")

#Bro Code's method
# username = input("Enter your name(12 character limit, without spaces and digits): ")

# if len(username) > 12:
#     print("Your username can't be more than 12 characters")
# elif not username.find(" ") == -1:
#     print("Your username can't contain spaces")
# elif not username.isalpha():
#     print("Your username can't contain numbers")
# else:
#     print(f"Welcome {username}")


#Indexing operator - access elements of a sequence using []
#[start : end : step]
cc_number = "1234-5678-9123-4567"
#print(cc_number[4])
#using start:end
#start is inclusive end is exclusive
#print(cc_number[5:9])
#you can use negative positions
#print(cc_number[-1])
#access by steps
#print(cc_number[::2])
#to invert a string
#cc_number = cc_number[::-1]
#print(f"{cc_number}")
#last digits
#cc_number = cc_number[-4:]
#print(cc_number)


#Format specifiers - {value:flags}
#format value based on flags
# .(number)f = round to that many decimal places
# :(number) = allocate that many spaces
# :03 = allocate and zero pad that many spaces
# :< = left justify
# :> = right justify
# :^ = center align
# :+ = use a plus sign to indicate positive value
# := = place sign to leftmost position
# : = insert a space before positive numbers
# :, = comma separator
#
# price1 = 12321.321
# price2 = -2912.233
# price3 = 42123.212
#decimal places
# print(f"Price 1 is ${price1:.1f}")
# print(f"Price 2 is ${price2:.1f}")
# print(f"Price 3 is ${price3:.1f}")
#spaces to show numbers
# print(f"Price 1 is ${price1:10}")
# print(f"Price 2 is ${price2:10}")
# print(f"Price 3 is ${price3:10}")
#add a 0 to zero pad the spaces
# print(f"Price 1 is ${price1:010}")
# print(f"Price 2 is ${price2:010}")
# print(f"Price 3 is ${price3:010}")
#justify to left center and right
# print(f"Price 1 is ${price1:<10}")
# print(f"Price 2 is ${price2:^10}")
# print(f"Price 3 is ${price3:>10}")
#preced a positive sign to positive numbers
# print(f"Price 1 is ${price1:+}")
# print(f"Price 2 is ${price2:+}")
# print(f"Price 3 is ${price3:+}")
#preced a space to positive numbers
# print(f"Price 1 is ${price1: }")
# print(f"Price 2 is ${price2: }")
# print(f"Price 3 is ${price3: }")
#each thousand separate by ,
#preced a positive sign to positive numbers
# print(f"Price 1 is ${price1:,}")
# print(f"Price 2 is ${price2:,}")
# print(f"Price 3 is ${price3:,}")
#a combination of flags
#preced a positive sign to positive numbers
# print(f"Price 1 is ${price1:+,.2f}")
# print(f"Price 2 is ${price2:+,.2f}")
# print(f"Price 3 is ${price3:+,.2f}")


#WHILE loops - loop code while a condition remains true
name = input("Enter your name: ")

while name == "":
    print("You didnt enter your name dumbass...")
    name = input("Another chance to enter your name: ")
print(f"Hi {name}")