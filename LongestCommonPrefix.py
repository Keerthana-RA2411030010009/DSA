class Solution:
    def LongestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return ""
        prefix = strs[0]
        for i in range(1, len(strs)):
            while strs[i].find(prefix) != 0:
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix

if __name__ == "__main__":
    solution = Solution()
    strs = input("Enter list of strings: ").split()
    print(solution.LongestCommonPrefix(strs))  # Example: ["flower","flow","flight"] -> "fl"
