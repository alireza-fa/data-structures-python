unsorted_list = [10, 5, 8, 4, 6, 1, 3, 7, 2, 9, -1]


for i in range(1, len(unsorted_list)):

    temp = unsorted_list[i]

    j = i - 1
    while j >= 0 and temp < unsorted_list[j]:
        unsorted_list[j + 1] = unsorted_list[j]
        j -= 1
    unsorted_list[j + 1] = temp


print(unsorted_list)
