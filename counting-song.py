def cycle_counting(people: int, beats: int) -> int:
    p_list = [x+1 for x in range(people)]
    index = 0
    while len(p_list) > 1:
        index = (index + beats - 1) % len(p_list)
        p_list.pop(index)
    return p_list[0]


def recur_counting(p_list: list, beats: int, index: int = 0) -> int:
    if len(p_list) == 1:
        return p_list[0]
    index = (index + beats - 1) % len(p_list)
    p_list.pop(index)
    return recur_counting(p_list, beats, index)


print(cycle_counting(int(input()), int(input())))
print(recur_counting([x+1 for x in range(int(input()))], int(input())))
