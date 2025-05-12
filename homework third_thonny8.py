def sum_range(a, b):
    if a > b:
        a, b = b, a
    total = 0
    for i in range(a, b + 1):
        total += i
    return total

print(sum_range(4,2))
print(sum_range(2,3))