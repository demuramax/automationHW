countries = ['Ukraine', 'Turkey', 'Tayland']
countries_dict = {'Ukraine': 'Kiev', 'Turkey': 'Ankara', 'Tayland': 'Bangkok'}

#1st variant:
print(f'{countries[0]}: {countries_dict[countries[0]]}')
print(f'{countries[1]}: {countries_dict[countries[1]]}')
print(f'{countries[2]}: {countries_dict[countries[2]]}')
print()
#2nd variant
for k, v in countries_dict.items():
    print(f'{k}: {v}')

