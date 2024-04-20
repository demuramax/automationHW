my_list = []
print('Add 3 elements to the list:')
my_list.append(int(input()))
my_list.append(int(input()))
my_list.append(int(input()))
print(my_list)

max_num = my_list[0]
for el in my_list:
    if el > max_num:
        max_num = el
print(f"max_num is {max_num}")


