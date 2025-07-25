number_of_stars = int(input("Please enter a number"))
for i in range(1, number_of_stars + 1):
    print("*" * i)
for i in range(1, number_of_stars):
    print("*" * (number_of_stars - i))
