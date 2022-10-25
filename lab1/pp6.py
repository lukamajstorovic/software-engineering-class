# Ask the user for a string and print out whether this string is a palindrome or not.

from math import floor


ulaz = input("Unesi rijec: ")

broj = floor(len(ulaz) / 2)

flag = 0

for x in range(broj):
    if ulaz[x] != ulaz[len(ulaz) - 1 - x]:
        flag = 1
if flag == 0:
    print("Rijec je palindrom.")
else:
    print("Rijec nije palindrom.")