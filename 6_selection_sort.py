unsorted_list = [10, 5, 8, 4, 6, 1, 3, 7, 2, 9, -1]

print(unsorted_list)


for i in range(0, len(unsorted_list)):
    for j in range(1 + i, len(unsorted_list)):
        if unsorted_list[i] > unsorted_list[j]:
            emp = unsorted_list[i]
            unsorted_list[i] = unsorted_list[j]
            unsorted_list[j] = emp


print(unsorted_list)
