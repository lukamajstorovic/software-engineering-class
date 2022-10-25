# Create a program that asks the user for a number and then prints out a list of all the divisors of that number.

x = int(input("Unesi broj: "))
divs = []

print("Djelitelji tog broja su: ")
counter = -1
for i in range(1, x):
    if x % i == 0:
        divs.append(i)
print(divs)
if len(divs) <= 1:
    print("Broj je prost.")
else:
    print("Broj nije prost.")