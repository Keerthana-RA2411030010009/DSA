class Solution:
    # self is a parameter
    # nums: list[int] and target: int are python syntaxes (parameter followed by datatype)
    # -> list [int] is again python sytax to indicate the return type of the function
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]+nums[j] == target:
                    return[i,j]
if __name__ == "__main__":
    solution = Solution()
    nums = list(map(int, input("Enter list: ").split()))
    target = int(input("Enter target: "))
    print(solution.twoSum(nums, target))  # [0, 1]

        