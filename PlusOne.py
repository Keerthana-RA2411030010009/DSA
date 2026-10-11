class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        s=""
        for i in range(len(digits)):
            s+=str(digits[i])
        return list(map(int, (s.split())))
if __name__ == "__main__":
    solution = Solution()
    digits = list(map(int, input("Enter list: ").split()))
    print(solution.plusOne(digits))  