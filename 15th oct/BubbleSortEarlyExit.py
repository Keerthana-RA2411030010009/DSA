arr= list(map(int, input("Enter list: ").split())) 
for i in range(len(arr)):
    swapped = False # loop can exit early if no swaps are made
    for j in range(len(arr) - 1):
        if arr[j] > arr[j + 1]:
            temp = arr[j]
            arr[j] = arr[j + 1]
            arr[j + 1] = temp
            swapped = True 
    if swapped == False:
        break

print(arr) 