# Номер успешной посылки 110174364
def count_platforms(weights: list, limit: int) -> int:
    weights.sort()
    start = 0
    end = len(weights) - 1
    platforms = 0
    while start <= end:
        if weights[start] + weights[end] <= limit:
            start += 1
        end -= 1
        platforms += 1
    return platforms


print(count_platforms(list(map(int, input().split())), int(input())))
