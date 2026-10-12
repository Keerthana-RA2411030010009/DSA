class Solution:
    def intersection(self, nums1: list[int], nums2: list[int]) -> list[int]:
        nums =[]
        for i in nums1:
            if i in nums2 and i not in nums: #avoid duplicates
                nums.append(i)
        return nums
if __name__ == "__main__":
    solution = Solution()
    nums1 = list(map(int, input("Enter first list: ").split()))
    nums2 = list(map(int, input("Enter second list: ").split()))
    print(solution.intersection(nums1, nums2))  