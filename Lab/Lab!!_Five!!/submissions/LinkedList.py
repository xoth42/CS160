import Person

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
    
    def delete(self, i):
        if i == 0:
            # get rid of front of list
            self.head = self.head.getNext()
            self.head.setPrevious(None)
        if i == self.size:
            # get rid of end of list
            self.tail = self.tail.getPrevious()
            self.tail.setNext(None)
        else:
            oneBeforeRemove = self.head
            # get rid of somehting in the middle 
            for _ in range(i-1):   
                oneBeforeRemove=oneBeforeRemove.getNext()
            #now, oneToRemove is the one that must be removed. now we must set the ones before and after this one to be eachother's next/previous
            oneBeforeRemove.setNext(oneBeforeRemove.getNext())
            oneBeforeRemove.getNext().setPrevious(oneBeforeRemove)
            
        
            

    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)

if __name__=="__main__":
    listOfPeople = LinkedList()
    listOfPeople.add(Person.Person("0", "Amherst"))
    listOfPeople.add(Person.Person("1", "Stow"))
    listOfPeople.add(Person.Person("2", "Malden"))
    print(listOfPeople)
    listOfPeople.delete(2)
    
    print(listOfPeople)
    
