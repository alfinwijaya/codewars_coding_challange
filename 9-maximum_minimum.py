def minimum(arr):
    min = arr[0]
    for i in range(1,len(arr)):
        min = arr[i] if arr[i] < min else min
    return min

def maximum(arr):
    max = arr[0]
    for i in range(1,len(arr)):
        max = arr[i] if arr[i] > max else max
    return max

print(minimum([-52, 56, 30, 29, -54, 0, -110]))
print(minimum([42, 54, 65, 87, 0]))
print(minimum([1, 2, 3, 4, 5, 10]))
print(minimum([-1, -2, -3, -4, -5, -10]))
print(minimum([9]))

print(maximum([-52, 56, 30, 29, -54, 0, -110]))
print(maximum([4,6,2,1,9,63,-134,566]))
print(maximum([5]))
print(maximum([534,43,2,1,3,4,5,5,443,443,555,555]))
print(maximum([9]))