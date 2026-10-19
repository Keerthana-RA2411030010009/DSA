def quick_sort(arr, low, high):
    if low >= high:
        return

    pivot = arr[low]
    lt = low # counts elements smaller than pivot
    i = low # current element
    gt = high # counts elements greater than pivot

    while i <= gt: # loop until current element is greater than gt
        if arr[i] < pivot: 
            arr[lt], arr[i] = arr[i], arr[lt] # if curr element is smaller than pivot, swap with lt
            lt += 1
            i += 1

        elif arr[i] > pivot: # if curr element is greater than pivot, swap with gt
            arr[i], arr[gt] = arr[gt], arr[i]
            gt -= 1

        else:
            i += 1

    quick_sort(arr, low, lt - 1)
    quick_sort(arr, gt + 1, high)


arr = list(map(int, input("Enter numbers separated by spaces: ").split()))
quick_sort(arr, 0, len(arr) - 1)
print(arr)