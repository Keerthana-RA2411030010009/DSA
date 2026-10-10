class Solution:
    def largest(self, arr):
        # code here
        max=arr[0] # make first element as default max
        if not arr: # return 0 if array is empty
            return 0
        for i in arr:
            if i > max:
                max=i # update max if current element is greater than max
        return max
            
if __name__ == "__main__":
    solution = Solution()
    arr = list(map(int, input("Enter list: ").split()))
    print(solution.largest(arr))  