def count_sheep(n):
    return ''.join(str(f'{x} sheep...') for x in range(1,n+1))

print(count_sheep(0))
print(count_sheep(1))
print(count_sheep(2))
print(count_sheep(3))