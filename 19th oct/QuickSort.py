def partition(arr, low, high): 
    pivot = arr[low] # initialize pivot as first element of the array
    i = low - 1 # counts elements smaller than pivot
    j = high + 1 # counts elements greater than pivot

    while True: # loop until i >= j
        i += 1
        while arr[i] < pivot: # move i until element greater than or equal to pivot is found
            i += 1

        j -= 1
        while arr[j] > pivot: # move j until element smaller than or equal to pivot is found
            j -= 1

        if i >= j:
            return j

        arr[i], arr[j] = arr[j], arr[i] # swap


def quick_sort(arr, low, high):
    if low < high:
        p = partition(arr, low, high)
        quick_sort(arr, low, p)
        quick_sort(arr, p + 1, high)


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print(arr)