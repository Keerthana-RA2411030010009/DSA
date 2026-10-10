class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        triangle = []
        for i in range(numRows):
            row = [1] * (i+1) # has 1 as default in all rows
            # 0th row has 1 element, 1st row has 2 elements, etc
            # so, ith row has i+1 elements
            for j in range(1, i): # skips first and last element bc they're always 1
                row[j] = triangle[i-1][j-1] + triangle[i-1][j] # core logic
            triangle.append(row)
        return triangle

if __name__ == "__main__":
    solution = Solution()
    numRows = int(input("Enter number of rows: "))
    print(solution.generate(numRows))