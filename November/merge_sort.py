# recursive sorting
# split array in half into a and b
# sort a, sort b, and then combine.
# merge sort a, merge sort b
# combine
def merge(a,b):
    newList = []
    i = 0
    while(i < len(a)+len(b)):
        if(a[i]<b[i]):
            newList.append(a[i])# pop is o(n)... oh no      
        else:
            newList.append(b[i])
        i+=1
    newList.extend(a)
    newList.extend(b) 
    return newList
def merge_sort(aList):
    if (len(aList) < 2):
        return(aList) 
    else:
        middle = len(aList)//2
        a = aList[0:middle]
        b = aList[middle:]
        aSorted = merge_sort(a)
        bSorted = merge_sort(b)
        # somehow combine them
        return merge(aSorted,bSorted)
        
        
if __name__=="__main__":
    alist=[99,37,-400,1,0,38,35,40,25]
    a = alist[0:len(alist)//2]
    b=alist[len(alist)//2:]
    #print(alist)
    #print(a,b)
    #merge_sort(alist)
    #print(alist)
    a.extend(b)
    a.extend([])
    print(a)
    print(merge_sort(a))
    print(a)
    