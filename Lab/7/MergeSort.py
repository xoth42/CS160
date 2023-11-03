'''
The complexity of pop is o(n), n being the length of the list.
tests for merge function: 
[1,2,3],[4,5,6] -> [1,2,3,4,5,6]
[0],[0] -> [0,0]
[0],[] -> [0]
[],[] -> []
[1,3,5][2] -> [1,2,3,5]

'''



def mergeSort(aList):
    if (len(aList) < 2):
        return(aList)
    else:
        a = aList[0:len(aList)//2]
        b = aList[len(aList)//2: len(aList)]
        aButSorted = mergeSort(a)
        bButSorted = mergeSort(b)
        return(merge(aButSorted, bButSorted))
        
def merge(listA, listB):
    newList = []
    nextA = 0
    nextB = 0 # nexta and nextb are the index of the next item to take from the list
    while(nextA < len(listA) and nextB < len(listB)):
        # untill one of the nextindexes reaches it's end, keep adding to newlist as each nextindex increases
        if(listA[nextA]<listB[nextB]):
            newList.append(listA[nextA])
            nextA+=1
        else:
            newList.append(listB[nextB])
            nextB+=1
    # one nextindex is at the end, and the other still has contents. extend them both (from nextindex to the end) to newlist
    newList.extend(listA[nextA:])
    newList.extend(listB[nextB:])
    # done!
    return(newList)
