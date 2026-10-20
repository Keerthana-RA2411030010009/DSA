n = int(input("Enter number of elements: "))
arr = list(map(int, input("Enter elements: ").split()))

max_val = max(arr)

count = [0] * (max_val + 1)

for num in arr: # count occurence of each element
    count[num] += 1

result = []

for i in range(len(count)): # append each element to result based on its count
    while count[i] > 0:
        result.append(i)
        count[i] -= 1

print("Sorted array:", result)