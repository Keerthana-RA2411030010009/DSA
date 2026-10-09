class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        if not strs:
            return "" # if there is no input in the list, automatically return an empty string
        prefix = strs[0]
        for i in range(1,len(strs)):
            while (strs[i].find(prefix)!=0):
                prefix = prefix[:-1] 
                # prefix[:-1] means - start at 0, end at index -1, which means, output will be the same string 
                # but without its last character (since stop value is always whatever no. we specify-1)
                if not prefix:
                    # if the prefix ends up being an empty string, exit
                    return ""
        return prefix
        


        
