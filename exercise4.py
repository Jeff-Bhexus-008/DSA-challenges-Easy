def count_even(numbers):
    total = 0

    for num in numbers:
        if num % 2 == 0:
            total += 1
    return total
print(count_even([1, 2, 3, 4, 6]))
print(count_even([1, 3, 5, 7]))