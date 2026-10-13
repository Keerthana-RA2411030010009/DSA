class Solution:
    def singleNumber(self, nums: list[int]) -> int:
        i=0
        single=[]
        while (i<len(nums)):
            if nums.count(nums[i])==1:
                return nums[i]
            i+=1
        

if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter list: ").split()))
    print(solution.singleNumber(nums))