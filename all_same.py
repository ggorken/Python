# Get the list
n = int(input("Enter the number of elements: "))
elements = []

while n:
    elements.append(int(input()))
    n -= 1

print(elements)

# print true if all elements are the same
# print false otherwise

if (len(elements) < 2):
    print("True")
else:
    print(elements.count(elements[0]) == len(elements))