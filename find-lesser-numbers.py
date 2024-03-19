def find_lesser(input_numbers: list) -> str:
    output_numbers = ''
    for i in range(len(input_numbers)):
        n = 0
        for j in range(len(input_numbers)):
            if input_numbers[i] > input_numbers[j]:
                n += 1
        output_numbers += str(n) + ' '
    output_numbers.rstrip()
    return output_numbers


print(find_lesser(list(map(int, input().split()))))
