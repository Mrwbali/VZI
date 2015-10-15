__author__ = 'Filip'


class Node:
    def __init__(self,dataInput):
        self.data = dataInput
        self.next = None


class LinkedList:

    def __init__(self):
        self.size = 0
        self.first = None
        self.currNode = None

    def isempty(self):
        if self.size is 0:
            return True
        else:
            return False

    def add(self,dataInput):
        if self.isempty() is True:
            newNode = Node(dataInput)
            self.currNode = newNode
            newNode.next = self.currNode
            self.first = newNode
            self.size = 1
            self.printList()
            return
        else:
            newNode = Node(dataInput)
            newNode.next = self.currNode.next
            self.currNode.next = newNode
            self.currNode = newNode
            self.size += 1
            self.printList()
            return

    def remove(self):
        if self.size is 1:
            self.currNode = None
            self.size = 0
            return
        else:
            tempNode = self.currNode.next
            self.next(self.size-1)
            self.currNode.next = tempNode
            self.size -= 1
            self.printList()
            return

    def printList(self):
        print()
        for i in range(self.size):
            self.next(1)
            if i is self.size-1:
                print(self.currNode.data, "<--")
            else:
                print(self.currNode.data)
        return

    def next(self,NumOfSteps):
        for i in range(NumOfSteps):
            self.currNode = self.currNode.next
        return

    def lookFor(self, lookForNubmer):
        for i in range(self.size):
            if self.currNode.data is lookForNubmer:
                self.printList()
                break
            else:
                self.next(1)
        return

# main

lst = LinkedList()

lst.add(1)
lst.add(2)
lst.add(3)
lst.add(4)
lst.add(5)

lst.printList()

lst.next(1)
lst.next(2)

lst.add(200)

lst.remove()

lst.lookFor(1)




