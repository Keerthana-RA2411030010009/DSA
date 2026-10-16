s=input("Enter a string: ")
count = {}
for ch in s: # count frequency of each character
    if ch in count:
        count[ch]+=1
    else:
        count[ch]=1

chars=list(count) # get count of unique characters

for i in range(len(chars)): # sort characters based on frequency
    for j in range(i+1, len(chars)):
        if count[chars[j]]>count[chars[i]]:
            temp=chars[i]
            chars[i]=chars[j]
            chars[j]=temp

result=""
for ch in chars:
    result+=ch*count[ch]

print(result)