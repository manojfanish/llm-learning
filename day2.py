# Week 1, Day 2
# Task: find the sum and the largest number in a list,
# WITHOUT using the built-in sum() or max().

numbers = [12, 7, 25, 3, 18]


def sum_and_largest(nums):
    total = 0
    largest = nums[0]  # start with the first number

    for n in nums:
        # TODO 1: add n to total
        # TODO 2: if n is bigger than largest, update largest
        pass

    return total, largest


result_sum, result_max = sum_and_largest(numbers)
print("Numbers:", numbers)
print("Sum:", result_sum)
print("Largest:", result_max)

# Expected output:
# Numbers: [12, 7, 25, 3, 18]
# Sum: 65
# Largest: 25