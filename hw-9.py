n = int(input('Enter n: '))

if n > 9 or n < 1:
    print('n would be between 1 and 9')
else:
    for x in range(1, n + 1):
        print("  " * (n - x), end="")
        for y in range(1, x + 1):
            print(y, end=" ")

        for y in range(x-1, 0, -1):
            print(y, end=' ')
        print()