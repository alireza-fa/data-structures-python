unsorted_list = [10, 5, 8, 4, 6, 1, 3, 7, 2, 9, -1]

print(unsorted_list)


for _ in range(1, len(unsorted_list)):
    for j in range(0, len(unsorted_list) - 1):
        if unsorted_list[j] > unsorted_list[j + 1]:
            unsorted_list[j], unsorted_list[j + 1] = unsorted_list[j + 1], unsorted_list[j]


print(unsorted_list)
