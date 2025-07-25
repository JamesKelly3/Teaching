numbers = [3, 50, 2, 72, 80, 72, 293884, 29148, 124452, 12, 2]
total = 0
for number in numbers:
    total += number
print("Sum:", total)
average = total / len(numbers)
print("Average:", average)
sorted_numbers = sorted(numbers)
median = sorted_numbers[int(len(sorted_numbers)/2)]
print("Median:", median)