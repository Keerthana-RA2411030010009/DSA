def SelectionSort(arr):
    n=len(arr)
    # traverse through all array elements
    for i in range(n-1): 
        minindex = i # assume the current position holds the minimum element
        for j in range(i+1, n): # test remaining unsorted elements
            if arr[j]<arr[minindex]:
                min_index=j
                
        # swap minimum element with first unsorted element
        if minindex!=i:
            arr[i],arr[minindex]=arr[minindex],arr[i]

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))
SelectionSort(numbers)
print("Sorted list: ",numbers)
