Time and Space Complexity
Time Complexity:

The function runs in O(n) time because it iterates through the list once to calculate the sum.

Space Complexity:

The function uses O(1) extra space because it only stores a few variables (n, expected_sum, actual_sum).

Edge Cases
Empty List:

If the input list is empty, the missing number is 1.

Single Element:

If the input list has only one element, the missing number is either 1 or 2, depending on the value of the element.

Missing Last Number:

If the missing number is n, the function will correctly identify it.
def find_missing_number(nums):
    # Calculate the expected length of the list (n)
    n = len(nums) + 1

    # Calculate the expected sum of numbers from 1 to n
    expected_sum = n * (n + 1) // 2

    # Calculate the actual sum of the numbers in the list
    actual_sum = sum(nums)

    # The missing number is the difference between the expected and actual sum
    return expected_sum - actual_sum

# Example 1
nums = [1, 2, 4, 5, 6]
print(find_missing_number(nums))  # Output: 3

# Example 2
nums = [1, 3, 4, 5, 6]
print(find_missing_number(nums))  # Output: 2

# Example 3
nums = [2, 3, 4, 5, 6]
print(find_missing_number(nums))  # Output: 1

Edge cases
def find_missing_number(nums):
    if not nums:
        return 1  # If the list is empty, the missing number is 1

    n = len(nums) + 1
    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum
