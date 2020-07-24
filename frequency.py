def Frequency:
    my_string = input('Enter a string : ')
    count = {}
    for i in my_string:
        if i in count:
            count[i] += 1
        else:
            count[i] = 1
    f = dict(sorted(count.items(), key = lambda x: x[1], reverse = True))
    for j, k in f.items():
        print(f"{j} = {k}")    
