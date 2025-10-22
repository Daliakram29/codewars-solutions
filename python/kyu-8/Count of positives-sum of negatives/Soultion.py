def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count = 0
    sum_num = 0

    for num in arr:
        if num > 0:
            count += 1

        elif num < 0:
            sum_num += num
    return [count, sum_num]
