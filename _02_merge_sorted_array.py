
class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> None:
        """
        Merge nums2 into nums1 as one sorted array in-place.

        Args:
        nums1 (list[int]): First sorted list with extra space at the end to hold nums2.
        m (int): Number of valid elements in nums1.
        nums2 (list[int]): Second sorted list.
        n (int): Number of elements in nums2.

        After function execution, nums1 contains all elements from nums1 and nums2 in sorted order.
        """
        p1 = m - 1        # Pointer for the last valid element in nums1
        p2 = n - 1        # Pointer for the last valid element in nums2
        p = m + n - 1     # Pointer for the last position in nums1 (including extra space)

        # Merge nums2 and nums1 starting from the end to avoid overwriting elements
        while p1 >= 0 and p2 >= 0:
            if nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]   # Put the larger element at the end of nums1
                p1 -= 1               # Move left in nums1
            else:
                nums1[p] = nums2[p2]  # Put the larger element from nums2
                p2 -= 1               # Move left in nums2
            p -= 1                   # Move left in the merged array position

        # If there are still elements left in nums2, copy them over
        while p2 >= 0:
            nums1[p] = nums2[p2]
            p2 -= 1
            p -= 1


# Example usage:
nums1 = [1, 3, 5, 0, 0, 0]  # m = 3 valid elements
nums2 = [2, 4, 6]           # n = 3 elements

solution = Solution()
solution.merge(nums1, 3, nums2, 3)

print("Merged array:", nums1)
