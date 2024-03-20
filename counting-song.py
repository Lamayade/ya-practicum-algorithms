def cycle_counting(people: int, beats: int) -> int:
    p_list = [x+1 for x in range(people)]
    index = 0
    while len(p_list) > 1:
        index = (index + beats - 1) % len(p_list)
        p_list.pop(index)
    return p_list[0]


def recur_counting(people: int, beats: int) -> int:
    print(people, beats)
    if people == 1:
        return 1
    return recur_counting(people - 1, beats) % people


print(cycle_counting(int(input()), int(input())))
print(recur_counting(int(input()), int(input())))
