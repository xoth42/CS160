class Node:
    def __init__(self, d = None):
        self.data = d
        self.next = None
        self.previous = None
        
    def setData(self, e):
        self.data = e

    def getData(self):
        return(self.data)

    def setNext(self, newNext):
        self.next = newNext

    def setPrevious(self, newPrevious):
        self.previous = newPrevious

    def getNext(self):
        return(self.next)
    
    def getPrevious(self):
        return(self.previous)
    
    def __str__(self):
        d = self.getData()
        #print(type(d))
        if type(d) == "NoneType":
            return("None")
        else:
            return(str(d))
    
if __name__=="__main__":
    print("Node.py is being run directly")
    Node1 = Node("Node1")
    print(Node1)