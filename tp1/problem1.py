def f(ch:str):
    li = list( map(int, ch.split() ) ) # O(n) parse input to number in a list
    index_list = [] #O(1)
    max_value = max(li) # O(n) find the max
    count = 0 #O(1)
    for i in range(len(li)): # O(n) loop over list
        if(li[i] == max_value): #O(1) find
            count = count + 1 #O(1)
            index_list.append(i) #O(1)
    if( count == 3 ):
        li.pop(index_list[-1]) #O(1)
    else:
        li.pop(index_list[0]) #O(1)

x = int(input()) #O(1)

for i in range(x): #O(n)
    f(input()) #O(n)