s = str.upper(input())

if len(s) == 1:
    print(s)
else:
    mydict = {}
    for i in s:
        mydict[i] = mydict.get(i, 0) + 1

    d = sorted(mydict.items(), key=lambda x: x[1], reverse=True)
    if d[0][1] == d[1][1]:
        print("?")
    else:
        print(d[0][0])
