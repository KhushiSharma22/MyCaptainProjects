n = int(input("Enter the number of elements: "))

mylist = [0,1]

if n > 2:
    for num in range(2,n):
        a = mylist[num-1] + mylist[num-2]
        mylist.append(a)
print(mylist)


# 0 1 1 2 3 5 8 13 21 34
