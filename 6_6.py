def lst_sort(numbers: list[int]) -> list[int]:
    sort_numbers: list = []
    for number in numbers:
        if number % 2:
            sort_numbers.append(number)
        else:
            sort_numbers.insert(0, number)
    return sort_numbers
