def count_occurrences(numbers, target):
    total = 0

    for num in numbers:
        if num == target:
            total += 1
    return total
print(count_occurrences([2, 5, 2, 8, 2], target = 2))
print(count_occurrences([1, 4, 7], target = 10))
