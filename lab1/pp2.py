# nAsk the user for a number. 
# Depending on whether the number is even or odd, 
# print out an appropriate message to the user. 

broj = int(input("Unesi broj: "))
if broj % 4 == 0:
    print("Broj je djeljiv s 4")
elif broj % 2 == 0:
    print("Broj je paran")
else:
    print("Broj je neparan")
# If the number is a multiple of 4, print out a different message.

