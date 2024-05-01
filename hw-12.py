# The program has a line `string`.
# Print the all words, containing the letter 'o' (in any case (upper/lower)) twice, as a title.

string = "This tool is cool. But that owl is awful. MAGIC TOOLS Ltd."
# Result: Tool Cool. Tools

result_lst = list()
for el in string.lower().split(' '):
    if 'oo' in el:
        result_lst.append(el.title())
print(*result_lst)
