# Find the sum and product of the elements of the list greater than the number MIN and less than the number MAX (both boundaries inclusive).
# If there are no such elements, print None object for both the sum and the product.
lst = [2, 4, 6, 2, 1, 1, 9, 4, 6]
MIN = 3
MAX = 6
...
# sum_ = 20, product = 576

filtered_list = [x for x in lst if MIN <= x <= MAX]

if filtered_list:
    sum_num = sum(filtered_list)
    product_num = 1
    for num in filtered_list:
        product_num *= num
else:
    # If there are no elements in the filtered list, set sum and product to None
    sum_num = None
    product_num = None

print("sum =", sum_num, ", product =", product_num)

