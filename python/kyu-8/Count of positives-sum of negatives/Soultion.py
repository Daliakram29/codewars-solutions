def count_positives_sum_negatives(arr):
    if not arr:
        return []

    count = 0
    sum_num = 0

    for num in arr:
        if num > 0:
            count += 1
#or positive_num=sum(1 for x in arr if x>0)

        elif num < 0:
            sum_num += num # negative_nums=sum(x for x in arr if x <0)
    return [count, sum_num]
