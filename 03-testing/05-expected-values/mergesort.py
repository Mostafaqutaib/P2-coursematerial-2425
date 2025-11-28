def split_in_two(ns):
    mid = len(ns) // 2
    return ns[:mid], ns[mid:]


def merge(left, right):
    if not left:
        return right

    if not right:
        return left

    if left[0] < right[0]:
        return [left[0]] + merge(left[1:], right)
    else:
        return [right[0]] + merge(left, right[1:])


def merge_sort(ns):
    if len(ns) <= 1:
        return ns

    left, right = split_in_two(ns)
    return merge(merge_sort(left), merge_sort(right))
