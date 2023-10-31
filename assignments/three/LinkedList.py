# feeling normal again
from Node import Node

# now we will make it so that linked lists contain nodes which contain data
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def length(self)->int:
        return self.size
    def add(self, data):
        e = Node(data)
        # e will become the node
        if self.size == 0:
            self.head = e
            self.tail = e
        else:
            current_last = self.tail
            current_last.setNext(e)
            e.setPrevious(current_last)
            self.tail = e
        self.size = self.size + 1
    def insert(self,distance:int,data):
        o = Node(data)
        location = self.head
        # wait! is this an edge case?
        if distance == 0:
            # insert at front of list
            o.setNext(self.head)
            self.head.setPrevious(o)
            self.head = o
            self.size+= 1
            return
        elif distance == self.size:
            # insert at end of list
            o.setPrevious(self.tail)
            self.tail.setNext(o)
            self.tail = o
            self.size+= 1
            return
       
        for i in range(distance-1):
            #print("i:",i)
            location = location.getNext()
        # insert in front of location
        #print("Location:",location)
        one_after_o = location.getNext()
        one_after_o.setPrevious(o)
        location.setNext(o)
        o.setNext(one_after_o)
        o.setPrevious(location)

        # o.setNext(location.getNext().getNext())
        # o.setPrevious(location)
        # location.setNext(o)
        # o.getNext().setPrevious(o)
        
        self.size+= 1

        
    def delete(self, i):
        #print(self.size, i)
        if i >= self.size-1:
            #raise IndexError("Index out of range")
            return
        elif self.size == 1:
            self.head = None
            self.tail = None
        elif i == 0:
            # get rid of front of list
            self.head = self.head.getNext()
            self.head.setPrevious(None)
        elif i == self.size-1: # index goes from 0 up
            # get rid of end of list
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        else:
             # get rid of somehting in the middle 
            remove_me = self.getNode(i)
            before = remove_me.getPrevious()
            after = remove_me.getNext()
            before.setNext(after)
            after.setPrevious(before)
            # done ^ 
            '''
            location_of_removal = self.head
            #print(self.head)
            for j in range(1,i):   
                #print("j:",j)
                location_of_removal=location_of_removal.getNext()
            #now we must set the ones before and after this one to be eachother's next/previous
            one_after_remove = location_of_removal.getNext()
            # location_of_removal.setNext(oneAfterRemove)
            one_before_remove = location_of_removal.getPrevious()
            # now set them equal
            one_after_remove.setPrevious(one_before_remove)
            one_before_remove.setNext(one_after_remove)
            #oneBeforeRemove.getNext().setPrevious(oneBeforeRemove) 
            '''
        self.size = self.size - 1 # need this
    def getNode(self,i):
        # index
        if i >= self.size-1:
            #raise IndexError("Index out of range")
            return None
        elif i == 0:
            return self.head
        elif i == self.size-1:
            return self.tail
        else:
            current = self.head
            for _ in range(i):
                current = current.getNext()
            return current
    def __getitem__(self, i):
        # not sure if this should return the node object, or its data
        if i == 0:
            return self.head.getData()
        elif i == self.size - 1:
            return self.tail.getData()
        else:
            current = self.head
            for _ in range(i):
                current = current.getNext()
            return current.getData()

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        for _ in range(self.size):
            stringToReturn = stringToReturn + "\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

            