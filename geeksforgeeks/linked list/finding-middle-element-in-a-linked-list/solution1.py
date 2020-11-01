# your task is to complete this function

'''
class node:
    def __init__(data):
        self.data = data
        self.next = None
'''

import math

# function should return index to the any valid peak element
def findMid(head):
    size = find_size(head)
    
    if size % 2 == 0:
        middle = size / 2 + 1
    else:
        middle = math.ceil(size / 2)
        
    current_node = head
    current = 1 # Problem constarint (1 <= N <= 5000)
    
    while current < middle:
        current = current + 1
        current_node = current_node.next
        
    return current_node.data
    


def find_size(head):
    size = 1 if head else 0
    
    next_node = head.next
    while next_node:
        size = size + 1
        next_node = next_node.next
        
    return size
    



#{ 
#  Driver Code Starts
# Node Class    
class node:
    def __init__(self, val):
        self.data = val
        self.next = None
        
# Linked List Class
class Linked_List:
    def __init__(self):
        self.head = None
        self.tail = None

    def insert(self, val):
        if self.head == None:
            self.head = node(val)
            self.tail = self.head
        else:
            new_node = node(val)
            self.tail.next = new_node
            self.tail = self.tail.next

def createList(arr, n):
    lis = Linked_List()
    for i in range(n):
        lis.insert(arr[i])
    return lis.head

if __name__=='__main__':
    t = int(input())
    for i in range(t):
        n = int(input())
        arr = list(map(int, input().strip().split()))
        head = createList(arr, n)
        print(findMid(head))

# } Driver Code Ends