def minmax(data):
    list1= []
    for i in range(len(data)):
        list1.append(data[i])
    list1.sort()
    tup= (list1[0],list1[-1])
    print(tup)
data=(8,9,17,29,47,0,1,69)
minmax(data)
