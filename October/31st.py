# Selection sort?
# look for the biggest, move to back. look everything -1 in the back, move biggest second to back
def put_biggest_at_end(alist, upToHere):
    next_index_to_look_in   = 1
    index_of_biggest        = 0
    while(next_index_to_look_in < upToHere):
        # could we insread use next ind < uptohere
        if(alist[next_index_to_look_in] > alist[index_of_biggest]):
            index_of_biggest = next_index_to_look_in
        next_index_to_look_in+=1
    # swap them
    temp = alist[upToHere]
    alist[upToHere] = alist[index_of_biggest]
    alist[index_of_biggest]=temp
    
def selectionSort(l):
    index_of_length_minus_sorted = len(l)-1
    for i in range(len(l)-1):
        put_biggest_at_end(l,index_of_length_minus_sorted)
        index_of_length_minus_sorted-=1
    
    
if __name__ =="__main__":
    l = [22, 13, 56, 0 ,-1 ,402, -24, 4000,1]
    selectionSort(l) # it works!
    print(l)
    put_biggest_at_end(l,len(l)-1)
    print(l)   
    put_biggest_at_end(l,len(l)-2)
    print(l)
    l1 = []
    put_biggest_at_end(l1,len(l)-1)
    print(l)
    