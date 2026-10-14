class Solution:
    def AlmostEquivalent(self, word1, word2):
        freq1=[0]*26
        freq2=[0]*26
        for ch in word1:
            freq1[ord(ch)-ord('a')]+=1
        for ch in word2:
            freq2[ord(ch)-ord('a')]+=1
        for i in range(26):
            if abs(freq1[i]-freq2[i])>3:
                return False

        return True
if __name__ == "__main__":
    solution = Solution()
    word1 = input("Enter first string: ")
    word2 = input("Enter second string: ")
    print(solution.AlmostEquivalent(word1, word2))