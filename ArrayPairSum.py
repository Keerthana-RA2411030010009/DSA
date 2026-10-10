class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort() # inbuilt function
        # sorting maximizes the total sum
        # ex: [1,4,3,2] gives (1,4)+(2,3) so total is 3. 
        # but sorted: [1,2,3,4] gives (1,2)+(3,4) so total is 4 -> more optimal

        return sum(nums[::2]) # sum of every even index number (min value of every pair)
if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter list: ").split()))
    print(solution.arrayPairSum(nums))  
