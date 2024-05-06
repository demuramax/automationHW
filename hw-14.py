# There is a list consisting of integer numbers.
# Create three lists:
# - to the first list add numbers that are only divisible by 3, but not divisible by 5
# - to the second list add numbers that are divisible by 5, but not divisible by 3
# - to the third list add numbers that are divisible by both 3 and 5

inp_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]  # Input list
# [3, 6, 9, 12]  # elements divided by 3
# [5, 10]  # elements divided by 5
# [0, 15]  # elements divided by 3 and by 5

list_divisible_by_3 = []
list_divisible_by_5 = []
list_divisible_by_3_and_5 = []

for el in inp_list:
    if el % 3 == 0 and el % 5 > 0:
        list_divisible_by_3.append(el)
    if el % 5 == 0 and el % 3 > 0:
        list_divisible_by_5.append(el)
    if el % 5 == 0 and el % 3 == 0:
        list_divisible_by_3_and_5.append(el)

print(*list_divisible_by_3)
print(*list_divisible_by_5)
print(*list_divisible_by_3_and_5)