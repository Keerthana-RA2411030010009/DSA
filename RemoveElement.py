class Solution:
    def RemoveElement(self, nums: list[int], val: int) -> list[int]:
        i = 0 # pointer that keeps track of every unique number. first number by default it unique
        if not nums:
            return 0 #edge case
        for j in range(len(nums)): # pointer that searches for next unique number
            if nums[j]!=val:
                nums[i]=nums[j] # replace next unique number after previous
                i+=1 # move pointer i

        return nums # no. of encountered unique numbers + first one
if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter list: ").split()))
    val = int(input("Enter value to remove: "))
    print(solution.RemoveElement(nums, val))  # Example: [3,2,2,3], val = 3 -> 2