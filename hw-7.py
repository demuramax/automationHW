size = int(input('Enter size of triangle: '))

#1st variant
counter = size
while counter > 0:
    print(' ' * (counter - 1) + '*'*(size - (counter-1)))
    counter -= 1

#2nd variant:
for i in range(size, 0, -1):
    print(' ' * (i - 1) + '*' * (size - (i - 1)))
