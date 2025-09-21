
def sort_massive(massive):
    if len(massive) <= 1:
        return massive

    division_element = massive[0]

    left_part = [el for el in massive if el < division_element]
    middle = [el for el in massive if el == division_element]
    right_part = [el for el in massive if el > division_element]

    return sort_massive(left_part) + middle + sort_massive(right_part)


print(sort_massive([1,10,3,8,1,1,5]))