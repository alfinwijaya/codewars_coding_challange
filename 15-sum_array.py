def sum_array(arr):
    if arr is None or len(arr) == 1:
        return 0
    return sum(j for i, j in enumerate(sorted(arr)) if i != 0 and i != len(arr)-1)

print(sum_array(None))
print(sum_array([]))
print(sum_array([6, 2, 1, 8, 10]))
print(sum_array([6, 0, 1, 10, 10]))
print(sum_array([-6, -20, -1, -10, -12]))
print(sum_array([-6, 20, -1, 10, -12]))