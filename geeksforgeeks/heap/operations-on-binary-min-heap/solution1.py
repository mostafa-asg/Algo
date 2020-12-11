#User function Template for python3

'''
heap = [0 for i in range(101)]  # our heap to be used
'''

def _heapify(node_index):
    global curr_size
    global heap

    left = node_index * 2 + 1
    right = node_index * 2 + 2

    min_index = node_index
    if left < curr_size and heap[left] < heap[node_index]:
        min_index = left

    if right < curr_size and heap[right] < heap[min_index]:
        min_index = right

    if min_index != node_index:
        # Swap values
        heap[node_index], heap[min_index] = heap[min_index], heap[node_index]
        _heapify(min_index)


def _shift_up(node_index):
    global heap
    global curr_size    

    if node_index > 0:
        parent = (node_index - 1) // 2

        if heap[parent] > heap[node_index]:
            heap[parent], heap[node_index] = heap[node_index], heap[parent]
            _shift_up(parent)


def insertKey (x):
    '''
    :param x: Insert value in heap.
    :return: None
    '''
    global heap
    global curr_size    

    heap[curr_size] = x    
    curr_size += 1

    _shift_up(curr_size-1)

def deleteKey (x):
    '''
    :param x: Index of value to be removed from heap.
    :return: None
    '''
    global heap
    global curr_size    
    
    if x >= curr_size:
        return

    heap[x] = -100000 # based on problem constraint
    _shift_up(x)
    extractMin()


def extractMin ():
    '''
    :return: return the minimum element from heap and remove it.
    '''    
    global heap
    global curr_size

    if curr_size == 0:
        return -1

    min_value = heap[0]

    heap[0], heap[curr_size-1] = heap[curr_size-1], heap[0]
    curr_size -= 1
    _heapify(0)

    return min_value





#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys

# Contributed by : Nagendra Jha

# _INPUT_LINES = sys.stdin.read().splitlines()
# input = iter(_INPUT_LINES).__next__
# _OUTPUT_BUFFER = io.StringIO()
# sys.stdout = _OUTPUT_BUFFER

# @atexit.register

# def write():
#     sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

heap = []  # our heap to be used
curr_size = 0  # current size of heap

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        n = int(input())
        a = list(map(int, input().strip().split()))
        # initialize every globals
        curr_size = 0
        heap = [0 for i in range(n)]
        i = 0
        while i < len(a):
            if a[i] == 1:
                insertKey(a[i + 1])
                i += 1
            elif a[i] == 2:
                deleteKey(a[i + 1])
                i += 1
            else:
                print(extractMin (), end=" ")
            i += 1
        # reinitialize every globals
        # curr_size = 0
        # heap = [0 for i in range(101)]
        print()
# } Driver Code Ends