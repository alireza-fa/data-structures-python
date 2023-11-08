unsorted_list = [10, 5, 8, 4, 6, 1, 3, 7, 2, 9, -1]

print(unsorted_list)


for i in range(len(unsorted_list)):
    min_index = i
    for j in range(i + 1, len(unsorted_list)):
        if unsorted_list[j] < unsorted_list[min_index]:
            min_index = j

    (unsorted_list[i], unsorted_list[min_index]) = (unsorted_list[min_index], unsorted_list[i])

print(unsorted_list)
