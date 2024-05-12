# There is a list of at least two float elements.
# Create a new list. It should contain elements of initial list, and between them should be added average of that elements.

lst = [1, 2, 3, 4, 5]
# Result: [1, 1.5, 2, 2.5, 3, 3.5, 4, 4.5, 5]

new_list = list()
for el in range(len(lst)):
    if lst[el] != lst[-1]:
        new_list.append(lst[el])
        new_list.append((lst[el] + lst[el+1])/2)
    else:
        new_list.append(lst[el])
print(new_list)

