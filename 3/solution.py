divisor = int(input("Enter a number:"))
acceptable_numbers = []
for i in range(100):
    if i % divisor == 0:
        acceptable_numbers.append(i)
print(acceptable_numbers)