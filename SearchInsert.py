class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        low = 0
        high = len(nums) - 1
        # use binary search bc constraint has O(log n)
        # linear is O(n)
        while low <= high:
            mid = (low + high) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                low = mid + 1
            else:
                high = mid - 1
                
        return low  # If not found, 'low' will point to the insertion index
if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter sorted list: ").split()))
    target = int(input("Enter target: "))
    print(solution.searchInsert(nums, target))  # Example: [1,3,5,6], target = 5 -> 2