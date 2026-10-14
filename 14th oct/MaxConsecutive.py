class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        left=0
        zeros=0
        max_len=0
        for right, num in enumerate(nums):
            if num==0:
                zeros+=1
            while zeros>k:
                if nums[left]==0:
                    zeros-=1
                left+=1
            max_len=max(max_len, right-left+1)
        
        return max_len

    
if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter list: ").split()))
    k = int(input("Enter k: "))
    print(solution.longestOnes(nums, k))