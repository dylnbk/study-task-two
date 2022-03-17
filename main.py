import random

#Task 1 – Variable types

def types():

    a, b, c, d = "Hello", 369, 3.69, True
    e, f, g, h = type(a), type(b), type(c), type(d)

    print(f"\n{a} - {e.__name__}\n{b} - {f.__name__}\
            \n{c} - {g.__name__}\n{d} - {h.__name__}\n")

#Task 2 – Police test

def police():

    print("\nPlease answer yes or no:\n")
    age = input("Are you over the age of 18?\n")
    time = input("Have you lived in the UK for the last 3 years?\n")
    remain = input("Do you have indefinite leave to remain and work in the UK?\n")
    qualify = input("Are you predicted or do you already hold a 2:2 degree or equivalent?\n")
    learn = input("Do you hold a level 3 qualification or an A-level equivalent\n")

    if  ( age[0].lower() == "y" and
         time[0].lower() == "y" and
       remain[0].lower() == "y" and
      qualify[0].lower() == "y" and
        learn[0].lower() == "y" ):
        print("\nYou can join the Police\n")
        
    else:
        print("\nYou cannot join the Police\n")

#Task 3 – Even odd count

def counting():

    nums, odd, even = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15], [], []

    print("\nNumbers:",", ".join([f"{x}" for x in nums]))

    for x in nums:
        if x % 2 != 0:
            odd.append(x)
        else:
            even.append(x)
    print(f"\nThere are {len(odd)} odd numbers in the list\
            \nThere are {len(even)} even numbers in the list\n")

#Task 4 – Sums

def sums(x):

    answer = sum(x)
    return answer

#Task 5 – Random number

def rand(y):

    result = random.choice(y)
    return result

#Task 6 – Colour to hex

def colours(z):

    colour = {
        "red":"#ff0000",
        "blue":"#00ff00",
        "green":"#0000ff",
        "orange":"#ffa500",
        "yellow":"#ffff00"
    }

    if z.lower() not in colour.keys():
        return "#000000"
    else:
        for x, y in colour.items():
            if z.lower() == x:
                return y

#Menu

def menu():

    choice = "y"

    while choice[0].lower() != "q":

        print("\n1. Variable types\n2. Police test\n3. Even odd count\
                \n4. Sums\n5. Random number\n6. Colour to hex\n7. Quit\n")

        choice = input("Which task would you like to run?\n")

        if choice == "1" or choice[0].lower() == "v":

            types()

        elif choice == "2" or choice[0].lower() == "p":

            police()

        elif choice == "3" or choice[0].lower() == "e":

            counting()

        elif choice == "4" or choice[0].lower() == "s":

            print(f"\n{sums([3,4,5,10,12,14])}\n")

        elif choice == "5" or choice[0].lower() == "r":

            print(f"\n{rand([3,6,9,34,76,54])}\n")

        elif choice == "6" or choice[0].lower() == "c":

            col = input("\nWhich colour hex would you like to see?\
             \n\nRed, Blue, Green, Orange or Yellow:\n")

            print(f"\n{colours(col)}\n")

        elif choice == "7" or choice[0].lower() == "q":

            print("\nProgram ended\n")
            break

        else:
            print("Invalid selection")

menu()
