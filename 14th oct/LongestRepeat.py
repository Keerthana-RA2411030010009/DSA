class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        count={}
        left=0
        max_freq=0
        max_len=0
        for right in range(len(s)):
            # adding current character to window count
            count[s[right]]=count.get(s[right], 0)+1
            
            # track max frequency of single character seen in current window
            max_freq = max(max_freq, count[s[right]])
            
            # current window size = right-left+1
            # remaining characters to change = window size-max_freq
            # if replacements needed > k, contract window from left
            if (right - left + 1) - max_freq > k:
                count[s[left]] -= 1
                left += 1
                
            # track max valid window size
            max_len = max(max_len, right-left+1)
            
        return max_len

if __name__ == "__main__":  
    solution = Solution()
    s = input("Enter string: ")
    k = int(input("Enter k: "))
    print(solution.characterReplacement(s, k))
