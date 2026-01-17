lst = [1, 2, 3, 4, 5]

length = len(lst)

if length == 0:
    result = [[], []]
else:
    middle = (length + 1) // 2
    first_part = lst[:middle]
    second_part = lst[middle:]
    result = [first_part, second_part]

print(result)
