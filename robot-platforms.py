# Номер успешной посылки 110264650
def count_platforms(weights_str: str, limit_str: str) -> int:
    weights = list(map(int, weights_str.split()))
    weights.sort()
    limit = int(limit_str)
    start = 0
    end = len(weights) - 1
    platforms = 0
    while start <= end:
        if weights[start] + weights[end] <= limit:
            start += 1
        end -= 1
        platforms += 1
    return platforms


if __name__ == '__main__':
    print(count_platforms(input(), input()))
