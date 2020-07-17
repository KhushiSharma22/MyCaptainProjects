mylist = []
n = int(input("Enter the number of elements to be included in the list: "))

for i in range(n):
    a = int(input(f"Enter the element {i+1} : "))
    mylist.append(a)
            
print(mylist)

list1 = []
for b in range(n):
    if mylist[b] == 0 or mylist[b] > 0:
          list1.append(mylist[b])

print(list1)
                       
