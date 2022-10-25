# Take a list,
# and write a program that prints out all the elements of the list that are less than 5.

# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
a = input("unesi brojeve odvojene zarezom: ")
a = [ int(x) for x in a.split(',') ]
m = [ x**2 for x in a if x < 5]
print(m)

n = []

for _ in a:
    if _ < 5:
        n.append(_)
print(n)

# Instead of printing the elements one by one, 
# make a new list that has all the elements less than 5 from this list in it and print out this new list.

#Write this in one line of Python.