def sort_containers(
        c_length: str,
        containers: str,
        m_length: str,
        matrix: str,
) -> str:
    c_list = list(map(int, containers.split()))
    m_list = list(map(int, matrix.split()))
    c_len = int(c_length)
    m_len = int(m_length)
    out_list = []
    for m_index in range(m_len):
        c_index = 0
        while c_index < c_len:
            if c_list[c_index] == m_list[m_index]:
                out_list.append(c_list[c_index])
                c_list.remove(c_list[c_index])
                c_len = len(c_list)
            else:
                c_index += 1
    c_list.sort()
    out_list.extend(c_list)
    return ' '.join(map(str, out_list))


print(sort_containers(input(), input(), input(), input()))
