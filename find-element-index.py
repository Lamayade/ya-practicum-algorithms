def find_or_guess_index(input_numbers: list, req_number: int):
    left = 0
    right = len(input_numbers)
    while left < right:
        mid = (left + right) // 2
        if input_numbers[mid] == req_number:
            return input_numbers.index(req_number)
        if input_numbers[mid] < req_number:
            left = mid + 1
        else:
            right = mid
    if req_number > input_numbers[mid]:
        return mid + 1
    return mid

print(find_or_guess_index(list(map(int, input().split())), int(input())))
