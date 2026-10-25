a = [2, 4, 6, 8, 10, 12, 14, 16, 18, 20]

total = 0
smallest = a[0]
largest = a[0]

for number in a:
    total = total + number

    if number < smallest:
        smallest = number

    if number > largest:
        largest = number

average = total / len(a)

print("Sum:", total)
print("Average:", average)
print("Smallest element:", smallest)
print("Largest element:", largest)