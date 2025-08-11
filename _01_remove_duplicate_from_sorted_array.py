
"""
def remove_duplicates(nums: list[int]) -> int:
    
    (Removes duplicates in-place from sorted list nums.
    Returns the new length k such that nums[:k] are the unique values.)
    
    if not nums:
        return 0

    write = 1  # next position to write a new unique value
    for read in range(1, len(nums)):
        if nums[read] != nums[read - 1]:
            nums[write] = nums[read]
            write += 1

    return write

"""



class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:   # <-- change here
        if not nums:
            print("The list is empty. Returning length = 0")
            return 0

        write = 1
        print(f"Initial array: {nums}")
        print(f"Start with write = {write}")

        for read in range(1, len(nums)):
            print(f"\nReading index {read}: value = {nums[read]}")

            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                print(f"Unique! Placing {nums[read]} at index {write}")
                write += 1
            else:
                print(f"Duplicate found: {nums[read]} (same as previous {nums[read - 1]}), skipping.")

            print(f"Current array: {nums}")
            print(f"write = {write}, read = {read}")

        print("\nFinished processing.")
        print(f"Unique length (k) = {write}")
        print(f"Unique elements = {nums[:write]}")
        return write

# Example usage:
nums = [1, 2, 2, 3, 3, 3, 4, 5, 5]
sol = Solution()
k = sol.removeDuplicates(nums)  # <-- also use camelCase here
print(f"\nReturned k = {k}")
print(f"Final array (first k elements are unique): {nums[:k]}")




# ================ Submitted Code ==============================
class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        if not nums:
            return 0

        write = 1

        for read in range(1, len(nums)):
            if nums[read] != nums[read - 1]:
                nums[write] = nums[read]
                write += 1

        return write

# Example usage:
nums = [1, 2, 2, 3, 3, 3, 4, 5, 5]
sol = Solution()
k = sol.removeDuplicates(nums)
print(f"Returned k = {k}")
print(f"Final array (first k elements are unique): {nums[:k]}")





       