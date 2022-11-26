# Input: head = [1,2,3,4,5]
# Output: [5,4,3,2,1]

# Input: head = [1,2]
# Output: [2,1]

# Input: head = []
# Output: []

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        
class LinkedList: 
    def __init__(self):
        self.head = None
        
    def print_llist(self):
        temp = self.head
        while(temp):
            print(temp.data)
            temp = temp.next
    
    def reverse_llist(self):
        if (self.head == None) or (self.head.next == None):
            return self.head
        else:
            currNode = self.head
            prevNode = None
            nextNode = None
            while(currNode):
                nextNode  = currNode.next  ### storing the next node value 
                currNode.next = prevNode  ### pointer to the previous node

                ###updating the node values
                prevNode = currNode
                currNode = nextNode
            self.head.next = None
            self.head = prevNode
            return self.head
            
if __name__ == "__main__":
    head = Node(1)
    second = Node(2)
    third = Node(3)
    fourth = Node(4)
    fifth = Node(5)

    llist = LinkedList()

    llist.head = head
    llist.head.next = second
    second.next = third
    third.next = fourth
    fourth.next = fifth

    print('Printing the values of Linked List')
    llist.print_llist()
    print("-"*100)
    print("Reversing the Linked List")
    llist.reverse_llist()
    llist.print_llist()