# Create a program that asks the user to enter their name and their age. 
# Print out a message addressed to them that tells them the year that they will turn 100 years old.

name = input("Unesi ime: ")
age = int(input("Unesi godine: "))
repeat = int(input("Unesi broj ponavljanja: "))
for _ in range(repeat):
    print(f"Bok {name}, imas {age} godina.")
    newage = 2022 - age + 100
    print(f"Imat ces {newage} godine 100 godina")

# Add on to the previous program by asking the user for another number 
# and printing out that many copies of the previous message.