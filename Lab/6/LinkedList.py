import Person
from Node import Node

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, e):
        newNode = Node(e)
        if self.size == 0:
            self.head = newNode
            self.tail = newNode
        else:
            current_last = self.tail
            current_last.setNext(newNode)
            newNode.setPrevious(current_last)
            self.tail = newNode
        self.size = self.size + 1

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        # don't do this
        # while (current != None)
        # while (current)
        while (current is not None):
        # like saying while (not(current is None))    
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)
    
    def swapDataWithNext(self, current:Node):
        old_data = current.getData()
        new_data = current.getNext().getData()
        current.setData(new_data)
        current.getNext().setData(old_data)
        
        '''
        currentFormerPrevious = current.getPrevious()
        former_next = current.getNext()
        current.setPrevious(former_next)
        current.setNext(former_next.getNext())
        # current's prev and next are bubbled now
        former_next.setNext(current)
        former_next.setPrevious(currentFormerPrevious)
        '''
        
        '''
        if current.getNext() == None:
            # cannot swap.
            return;
        if current.getNext() == selt.tail:
            # next is tail, so current must become tail.
            if current == self.head:
                #switching head and tail
                self.tail = current
                self.head = current.getNext()
                current.setPrevious(self.head)
                current.setNext(None)
                self.head.setNext(self.tail)
                self.head.setPrevious(None)
            else:
                # switching current and tail
                current.getPrevious().setNext(current.getNext())
                self.tail = current
                current.setPrevious(current.getNext())
                '''
            
    
    def bubble_once(self):
        if (self.size <= 1):
            return
        if (self.size == 2):
            if (self.head.getData() > self.tail.getData()):
                self.swapDataWithNext(self.head)
            return
        else:
            current = self.head
            for i in range(self.size - 1):
                if (current.getData() > current.getNext().getData()):
                    self.swapDataWithNext(current)
                current = current.getNext()
            #reached the end of the list? -> todo test
    def bubble(self):
        for i in range(self.size):
            self.bubble_once()

        '''
        if not self.size < 2:
            current_test = self.head
    
            while (current_test != self.tail):
                if (current_test.getData() > current_test.getNext().getData()):
                    # current data is larger than next data, so they need to swap.
                    
                    new_previous = current_test.getNext()
                    #edge cases:
                    # if (current_test == self.head):
                    #     if 
                    #     current_test.setNext
                    '''

if __name__ == "__main__":
    # listOfPeople = LinkedList()
    # listOfPeople.add(Person.Person("Jaime"))
    # listOfPeople.add(Person.Person("Maria"))
    # listOfPeople.add(Person.Person("Maria"))
    # print(listOfPeople)
    
    myList = LinkedList()
    myList.add(40)
    myList.add(2)
    myList.add(3)
    myList.add(1)
    
    #print(myList)
    #myList.swapDataWithNext(myList.head)
    print(myList)
    # Testing bubble sort
    
    myList.bubble()
    print(myList)