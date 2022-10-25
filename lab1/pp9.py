import random


x = random.randint(1, 9)

ulaz = input("Unesi: ")

counter = 0

while(ulaz != "exit"):
    if int(ulaz) == x:
        print("Tocno.")
        counter += 1
    elif int(ulaz) > x:
        print("Previsoko.")
        counter += 1
    else:
        print("Prenisko.")
        counter += 1
    ulaz = input("Unesi: ")
print(f"Uzeo si {counter} pokusaja")