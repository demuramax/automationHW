#HW-2:
cat_lst = ['pushok', 'murka', 'maya']
#1st variant:
print(f'{cat_lst[0]}, {cat_lst[1]}, {cat_lst[2]}')
#2nd variant:
print(*cat_lst, sep=', ')
#3nd variant:
print(', '.join(cat_lst))



