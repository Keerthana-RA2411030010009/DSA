'''class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record=[]
        for i in range(len(operations)):
            
            if operations[i] in ['C','c']:
                record.pop()
            elif operations[i] in ['D', 'd']:
                if len(record)>=1:
                    record.append(record[-1]*2)
            elif operations[i]=="+":
                if len(record)>=2:
                    record.append(record[-1]+record[-2])
            # the reason why we don't check for integer first:
            # we use isdigit() to check
            # but isdigit flags negative numbers as false because '-' is not a digit
            # so by assuming that once all the other operations are taken care of
            # the last remaining ones are going to be integers
            # covert them all to int and add to record
            # but this will not return anything properly if operations has anything
            # other than [c,d,+ and int]
            # hence, use try except block
            # try converting all elements in operations to int
            # if it throws value error, do the rest of the if-elif conditions
            else:
                record.append(int(operations[i]))
        return sum(record)'''

class Solution:
    def calPoints(self, operations: list[str]) -> int:
        record=[]
        for i in range(len(operations)):
            try: # try converting all elements to int
                record.append(int(operations[i]))
            except ValueError: # perform other operations to elements that aren't int
                if operations[i] in ['c','C']:
                    if len(record)>=1:
                        record.pop()
                elif operations[i] in ['d','D']:
                    if len(record)>=1:
                        record.append(record[-1]*2)
                elif operations[i]=="+":
                    if len(record)>=2:
                        record.append(record[-1]+record[-2])
        return sum(record)

if __name__ == "__main__":
    solution = Solution()
    operations = input("Enter operations: ").split()
    print(solution.calPoints(operations))  