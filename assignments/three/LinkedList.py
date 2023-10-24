# feeling normal again
class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0
    def add(self, e):
        if self.size == 0:
            self.head = e
            self.tail = e
        else:
            current_last = self.tail
            current_last.setNext(e)
            e.setPrevious(current_last)
            self.tail = e
        self.size = self.size + 1
    def insert(self,distance:int,o):
        location = self.head
        for i in range(distance):
            location = location.getNext()
        # insert in front of location
        location.getNext().setPrevious(o)
        location.setNext(o)
        o.setNext(location.getNext().getNext())
        o.setPrevious(location)
        self.size+= 1
        
    def delete(self, i):
        if self.size == 1:
            self.head = None
            self.tail = None
        elif i == 0:
            # get rid of front of list
            self.head = self.head.getNext()
            self.head.setPrevious(None)
        elif i == self.size - 1: # size goes from 1 up, index goes from 0 up
            # get rid of end of list
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        else:
             # get rid of somehting in the middle 
            oneBeforeRemove = self.head
            for _ in range(i-1):   
                oneBeforeRemove=oneBeforeRemove.getNext()
            #now, oneToRemove is the one that must be removed. now we must set the ones before and after this one to be eachother's next/previous
            oneAfterRemove = oneBeforeRemove.getNext().getNext()
            oneBeforeRemove.setNext(oneAfterRemove)
            oneAfterRemove.setPrevious(oneBeforeRemove)
            #oneBeforeRemove.getNext().setPrevious(oneBeforeRemove) 
        self.size = self.size - 1 # need this

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

            