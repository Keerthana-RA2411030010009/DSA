class Solution:
    def removeDuplicates(self, nums: list[int]) -> list[int]:
        i = 0 # pointer that keeps track of every unique number. first number by default it unique
        if not nums:
            return 0 #edge case
        for j in range(1, len(nums)): # pointer that searches for next unique number
            if nums[i]!=nums[j]:
                i+=1 # move pointer i
                nums[i]=nums[j] # replace next unique number after previous

        return nums # no. of encountered unique numbers + first one

if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter list: ").split()))
    print(solution.removeDuplicates(nums))  # Example: [1,1,2] -> 2