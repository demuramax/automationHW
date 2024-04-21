# The user enters the minimum and maximum width of the diamond pattern.
# Print a "diamond" with given dimensions composed of '*' symbols.
# If the entered minimum width is greater than the maximum width, print a warning and terminate the program.
# If the difference between the maximum and minimum widths is not a multiple of 2, print a warning and terminate the program.

min_width = int(input('Enter minimal width: '))
max_width = int(input('Enter maximus width: '))

if min_width > max_width:
    print('Minimum width would be less than maximum width.')
if (max_width - min_width) % 2 != 0:
    print('Difference between max and min width would be divisible by 2')

for x in range(min_width, max_width + 1, 2):
    if x == min_width:
        print(" " * ((max_width - x) // 2) + '*' * x)
    else:
        print(" " * ((max_width - x) // 2) + '*' + ' ' * (x-2) + '*')

for y in range(max_width-2, min_width-1, -2):
    if y == min_width:
        print(" " * ((max_width - y) // 2) + '*' * y)
    else:
        print(" " * ((max_width - y) // 2) + '*' + ' ' * (y - 2) + '*')
