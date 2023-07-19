def top_k(lst, k):
    values = []
    greatest = lst[0]
    while len(values) < k:
        for item in lst:
            if item > greatest:
                greatest = item
        lst.remove(greatest)
        values.append(greatest)
        greatest = lst[0]
    return values
assert top_k([9, 9, 4, 9, 7, 9, 3, 1, 6], 5) == [9, 9, 9, 9, 7]
assert top_k([9, 8, 4, 5, 7, 2, 3, 1, 6], 5) == [9, 8, 7, 6, 5]
assert top_k([4, 5, 2, 3, 1, 6], 6) == [6, 5, 4, 3, 2, 1]
assert top_k([4, 5, 2, 3, 1, 6], 3) == [6, 5, 4]
assert top_k([4, 5, 2, 3, 1, 6], 0) == []
