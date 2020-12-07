# Your task is to complete this function

'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

'''

# This function should rotate list counter-
# clockwise by k and return head node
def rotateList(head, k):
    current_node = head
    prev_node = None
    new_head= None
    last_node = None
    counter = 0

    while current_node != None:
        prev_node = current_node
        current_node = current_node.next
        counter += 1

        if counter == k:
            new_head = current_node
            last_node = prev_node

    if new_head != None:
        prev_node.next = head
        last_node.next = None
        head = new_head
    
    return head 





#{ 
#  Driver Code Starts
# driver

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    
    def insert(self,val):
        if self.head is None:
            self.head = Node(val)
            self.tail = self.head
        else:
            self.tail.next = Node(val)
            self.tail = self.tail.next

def printList(n):
    while n:
        print(n.data, end=' ')
        n = n.next
    print()

if __name__=="__main__":
    for _ in range(int(input())):
        n = int(input())
        arr = [int(x) for x in input().split()]
        k = int(input())
        
        lis = LinkedList()
        for i in arr:
            lis.insert(i)
        
        head = rotateList(lis.head,k)
        printList(head)
# } Driver Code Ends