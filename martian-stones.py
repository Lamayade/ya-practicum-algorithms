def count_fit_stones(
        req_count: int,
        req_seq: list,
        sam_count: int,
        sam_seq: list,
):
    sam_seq_sorted = sorted(sam_seq, reverse=True)
    req_seq_sorted = sorted(req_seq, reverse=True)
    happy_clients_count = 0
    inx = 0
    while inx < min(len(sam_seq_sorted), len(req_seq_sorted)):
        if req_seq_sorted[inx] <= sam_seq_sorted[inx]:
            happy_clients_count += 1
        else:
            del req_seq_sorted[inx]
            inx -= 1
        inx += 1
    return happy_clients_count


print(
    count_fit_stones(
        int(input()),
        list(map(int, input().split())),
        int(input()),
        list(map(int, input().split())),
    )
)
