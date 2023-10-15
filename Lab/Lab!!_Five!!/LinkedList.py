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

            
        """
        else:
          oneToRemove = self.head
            # get rid of somehting in the middle 
            # head <-> b <-> c <-> d <-> e ...
            # ^ oneToRemove (head)
            for _ in range(i):   
                oneToRemove=oneToRemove.getNext()
            # head <-> b <-> c <-> d ..... pre <-> i <-> post ....
            #                                      ^ oneToRemove (i)
            #now, oneToRemove is the one that must be removed. now we must set the ones before and after this one to be eachother's next/previous
            # pre <-> oneToRemove <-> post
            pre = oneToRemove.getPrevious()
            post = oneToRemove.getNext()
            # pre <-> post -X- oneToRemove
            pre.setNext(post)
            post.setPrevious(pre)
            
            # oneToRemove.setNext(None)
            # oneToRemove.setPrevious(None)
        """
        
        
    def __str__(self):
        stringToReturn = "List size: " + str(self.size)
        current = self.head
        while (current is not None):
            stringToReturn = stringToReturn + "\n\n" + str(current)
            current = current.getNext()
        return(stringToReturn)


import unittest
class fuckingTestWhore(unittest.TestCase):
    # i'm really mad today
    def testList(self):
        listOfLinks = LinkedList()
        p1 = Person.Person("0", "Amherst")
        listOfLinks.add(Person.Person("0", "Amherst"))
        listOfLinks.add(Person.Person("1", "Stow"))
        listOfLinks.add(Person.Person("2", "Malden"))
     
        self.assertEqual(listOfLinks.size,3)
        self.assertEqual(listOfLinks.head,p1)
        listOfLinks.delete(2)
        self.assertEqual(listOfLinks.size,2)
        self.assertEqual(listOfLinks.head,p1)
        
if __name__=="__main__":
    

    
    listOfPeople = LinkedList()
    listOfPeople.add(Person.Person("0", "Amherst"))
    listOfPeople.add(Person.Person("1", "Stow"))
    listOfPeople.add(Person.Person("2", "Malden"))
    print("Starting List:\n",listOfPeople)
    deleteIndex = 1
    print(f"deleting index {deleteIndex}")
    listOfPeople.delete(deleteIndex)
    print("List Post Deletion:\n", listOfPeople)
    deleteIndex = 1
    print(f"deleting index {deleteIndex}")
    listOfPeople.delete(deleteIndex)
    print("List Post Deletion:\n", listOfPeople)
    unittest.main()
