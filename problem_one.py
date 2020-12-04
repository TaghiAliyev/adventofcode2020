# Given list of numbers, find two that sum up to 2020 and multiple them
import numpy as np
list_of_numbers = np.loadtxt('problem_one_input.txt')

def find_sum_in_sorted_list(sorted_list, sum):
    left_start = 0
    right_start = len(sorted_list) - 1
    while left_start < right_start:
        if sorted_list[left_start] + sorted_list[right_start] == sum:
            return sorted_list[left_start] * sorted_list[right_start]
        elif sorted_list[left_start] + sorted_list[right_start] > sum:
            right_start -= 1
        else:
            left_start += 1
    return None

# Sorting makes the search simpler.
sorted_list = sorted(list_of_numbers)

print('Finding two numbers combination')
print(f'Found sum is: {find_sum_in_sorted_list(sorted_list, 2020)}')
print('Finding three numbers combination')
# three numbers that add up. Idea is this: For each number, create complement set, and then try to find 2 numbers
# excluding that number that sum up to the complement
# The complement list is also sorted.
complement_set = [abs(x - 2020) for x in sorted_list]
for i in range(len(complement_set)):
    sum_to_find = complement_set[i]
    copy_list = sorted_list.copy()
    del copy_list[i]  # Remove the element that should not be considered for the sum
    # copy list is still sorted, so the smart search can be done by pushing from two sides
    sum_found = find_sum_in_sorted_list(copy_list, sum_to_find)
    if sum_found is not None:
        print(f'Found sum is: {sum_found * sorted_list[i]}')
        break

