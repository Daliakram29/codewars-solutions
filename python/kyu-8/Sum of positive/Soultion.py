def positive_sum(arr):
    if not arr:
        return 0
    positive_nums = sum(x for x in arr if x > 0)

    return positive_nums
