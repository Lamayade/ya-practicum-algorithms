def valid_mountain_array(arr: list) -> bool:
    length = len(arr)
    if arr[0] > arr[1]:
        return False
    if arr[length-1] > arr[length-2]:
        return False
    for i in range(length-1):
        if arr[i] > arr[i+1]:
            for j in range(i+1, length-1):
                if arr[j+1] >= arr[j]:
                    return False
            return True
        if arr[i] == arr[i+1]:
            return False
    return False


print(valid_mountain_array(list(map(int, input().split()))))
