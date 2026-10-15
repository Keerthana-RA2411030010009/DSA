n=int(input("Enter number of elements: "))
arr=[]
for i in range(n):
    num=int(input("Enter number: "))
    arr.append(num)
for i in range(n):
    for j in range(n-1-i):
        if arr[j]%2!=0 and arr[j+1]%2==0: # if odd number is in front of an even number
            # they are in the wrong order according to this rule
            temp=arr[j] # so swap using temp variable
            arr[j]=arr[j+1]
            arr[j+1]=temp

print(arr)