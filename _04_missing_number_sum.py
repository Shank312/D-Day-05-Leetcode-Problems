
class Solution:
    def missingNumber(self, nums):
        # n is the length of list nums
        n = len(nums)
        print(f"Length of the input list (n): {n}")

        # Calculate the sum of numbers from 0 to n using the formula: (n*(n+1))//2
        expected_sum = (n * (n + 1)) // 2
        print(f"Expected sum of the numbers from 0 to {n}: {expected_sum}")

        # Calculate the actual sum of the elements present in the list
        actual_sum = sum(nums)
        print(f"Actual sum of elements in list: {actual_sum}")

        # The missing number is the difference between expected sum and actual sum
        missing = expected_sum - actual_sum
        print(f"Missing number: {missing}")

        return missing

sol = Solution()
print(sol.missingNumber([0, 1, 3, 4]))  # Expected output: 2

