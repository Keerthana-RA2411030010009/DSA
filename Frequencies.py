class Solution:
    def findDiff(self, arr):
        
        if not arr: # edge case
            return 0
        
        frequency = {} # count frequencies using a standard dictionary
        for num in arr:
            if num in frequency:
                frequency[num] += 1
            else:
                frequency[num] = 1

        # if there's only one unique type of element return 0
        if len(frequency) <= 1:
            return 0

        # find the highest and lowest occurrences
        max_count = float('-inf')
        min_count = float('inf')

        for count in frequency.values():
            if count > max_count:
                max_count = count
            if count < min_count:
                min_count = count
        return max_count - min_count
  
if __name__ == "__main__":
    solution = Solution()
    arr = list(map(int, input("Enter list: ").split()))
    print(solution.findDiff(arr)) 