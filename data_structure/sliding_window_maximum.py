def sliding_window_max(num_list, k):
    if not num_list or k <= 0:
        return []

    result = []
    n = len(num_list)

    for i in range(n - k + 1):
        window = num_list[i:i + k]
        max_value = max(window)
        result.append(max_value)

    return result


if __name__ == "__main__":
    num_list = [3, 4, 5, 1, -44, 5, 10, 12, 33, 1]
    k = 3
    output = sliding_window_max(num_list, k)
    print(output)
