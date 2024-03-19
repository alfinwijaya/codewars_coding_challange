def snail(snail_map):
    result = []

    top = 0
    bottom = len(snail_map) - 1
    left = 0 
    right = len(snail_map[0]) - 1
    total_items = len(snail_map) * len(snail_map[0])

    while(True):

        for i in range(left, right+1):
            result.append(snail_map[top][i])
        top += 1
        if len(result) == total_items:
            break

        for i in range(top, bottom+1):
            result.append(snail_map[i][right])
        right -= 1
        if len(result) == total_items:
            break

        for i in range(right, left-1, -1):
            result.append(snail_map[bottom][i])
        bottom -= 1
        if len(result) == total_items:
            break

        for i in range(bottom, top-1, -1):
            result.append(snail_map[i][left])
        left += 1
        if len(result) == total_items:
            break

    return result


print(snail([[1,2,3],[8,9,4],[7,6,5]]))