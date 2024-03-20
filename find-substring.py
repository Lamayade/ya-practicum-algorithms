def find_unique_symbols_length(input_seq: str) -> int:
    symbols_with_index = {}
    max_length = 0
    start = 0
    for end in range(len(input_seq)):
        if input_seq[end] in symbols_with_index:
            start = max(start, symbols_with_index[input_seq[end]] + 1)
        symbols_with_index[input_seq[end]] = end
        max_length = max(max_length, end - start + 1)
    return max_length


print(find_unique_symbols_length(input()))
