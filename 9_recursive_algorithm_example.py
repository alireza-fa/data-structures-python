def rec_factorial(number) -> int:
    if number == 1:
        return number

    return number * rec_factorial(number - 1)


print(rec_factorial(number=1000))


def sum_int_list(array: list, length: int) -> int:
    if length <= 0:
        return 0
    return array[length - 1] + sum_int_list(array=array, length=length - 1)


def find_number(array: list, number: int) -> bool:
    if len(array) == 1:
        return bool(array[0] == number)

    half_len = len(array) // 2
    if array[half_len] == number:
        return True

    if array[half_len] < number:
        return find_number(array=array[half_len:], number=number)
    else:
        return find_number(array=array[0:half_len], number=number)


def find_max(array: list):
    if len(array) == 1:
        return array[0]

    half_len = len(array) // 2
    first_half = find_max(array=array[:half_len])
    second_half = find_max(array=array[half_len:])

    return max([first_half, second_half])


if __name__ == '__main__':
    # print(find_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13], number=5))
    print(find_max(array=[1, 2, 5, 4, 88, 41, 6, 9, 0, 11, -666]))
