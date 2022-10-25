# a = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89]
# b = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

import random

def generate_random_list(num_el, lower, upper):
    length = random.randint(5, num_el)
    lista = []
    for x in range(length):
        lista.append(random.randint(lower, upper))
    return lista


a = []
b = []
c = []

a = generate_random_list(15, 0, 10)
b = generate_random_list(20, 0, 20)

print(sorted(a))
print(sorted(b))

for x in a:
    if x in b and x not in c:
            c.append(x)
print(sorted(c))