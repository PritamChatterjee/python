# DSA Example: Linear Search

numbers = [10, 25, 30, 45, 50, 65, 70]

target = 45

found = False

for i in range(len(numbers)):
    if numbers[i] == target:
        print("Element found!")
        print("Element:", target)
        print("Index:", i)
        found = True
        break

if found == False:
    print("Element not found")