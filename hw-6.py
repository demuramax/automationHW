height = int(input('Enter height of rectangular: '))
width = int(input('Enter width of rectangular: '))
symbol = input('Enter symbol to build rectangular with: ')

for x in range(height):
    print(symbol * width)