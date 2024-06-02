# There is a list consisting of dictionaries. Each dictionary describes a user and
# has two keys: 'name' (str) and 'age' (int).
# Create and output a list of users' names whose age is 18 years (including) or older.

users = [
    {'name': 'Luarvik L. Luarvik',
     'age': 17},
    {'name': 'Olaf Andvarafors',
     'age': 18},
    {'name': 'Brun Du Barnstokr',
     'age': 19}
]

Result: ['Olaf Andvarafors', 'Brun Du Barnstokr']
names_list = []
for x in users:
    if x['age'] > 17:
        names_list.append(x['name'])
print(names_list)