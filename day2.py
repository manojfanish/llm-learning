# Week 1, Day 2
# Task: find the sum and the largest number in a list,
# WITHOUT using the built-in sum() or max().

numbers = [12, 7, 25, 3, 18]
# numbers = [-5,-2,-9]


def sum_and_largest(nums):
    total = 0
    largest = nums[0]  # start with the first number

    for n in nums:
        total = total + n # TODO 1: add n to total
        if n > largest: # TODO 2: if n is bigger than largest, update largest
            largest = n

    return total, largest

total, largest = sum_and_largest(numbers)
print("Numbers:", numbers)
print("Sum:", total)
print("Largest:", largest)

# result_sum, result_max = sum_and_largest(numbers)
# print("Numbers:", numbers)
# print("Sum:", result_sum)
# print("Largest:", result_max)

# Expected output:
# Numbers: [12, 7, 25, 3, 18]
# Sum: 65
# Largest: 25