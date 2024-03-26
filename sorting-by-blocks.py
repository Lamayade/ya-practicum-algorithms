def sort_blocks(block_len_string: str, block_seq_string: str) -> int:
    block_len = int(block_len_string)
    block_seq = list(map(int, block_seq_string.split()))
    block_count = 1
    next_block = 1
    for block_index in range(block_len):
        next_block -= 1 if next_block > 0 else 0
        if block_seq[block_index] == block_index and next_block == 0:
            block_count += 1
        if block_seq[block_index] > block_index:
            next_block = max(next_block, block_seq[block_index] - block_index)
        if block_seq[block_index] == block_len - 1:
            return block_count


print(sort_blocks(input(), input()))
