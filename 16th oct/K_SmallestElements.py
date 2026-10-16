def K_SmallestElements(arr, k):
    n=len(arr)
    k=min(k, n) # edge case, if k>n
    for i in range(k):
        minindex=i
        
        # for remaining unsorted array,
        for j in range(i+1, n):
            if arr[j]<arr[minindex]:
                minindex=j
                
        # swap min and current position
        if minindex!=i:
            arr[i],arr[minindex]=arr[minindex],arr[i]
            
    # first k elements are now k smallest elements
    return arr[:k]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
k_val = int(input("Enter the value of k: "))
smallestElements = K_SmallestElements(numbers, k_val)
print(f"The {k_val} smallest elements are:", smallestElements)
