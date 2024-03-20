# Номер успешной посылки 110213198
def count_platforms(weights: str, limit: str) -> int:
    w = list(map(int, weights.split()))
    w.sort()
    l = int(limit)
    start = 0
    end = len(w) - 1
    platforms = 0
    while start <= end:
        if w[start] + w[end] <= l:
            start += 1
        end -= 1
        platforms += 1
    return platforms


if __name__ == '__main__':
	print(count_platforms(input(), input()))