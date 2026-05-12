def list_sum(numbers):
    total = sum(numbers)
    return total
n = int(input("Enter number of elements: "))

numbers = []

for i in range(n):
    num = int(input("Enter element: "))
    numbers.append(num)
result = list_sum(numbers)

print("Sum of list elements is:", result)
