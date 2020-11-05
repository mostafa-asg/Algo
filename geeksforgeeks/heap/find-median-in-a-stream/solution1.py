#User function Template for python3
def balanceHeaps():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    Balance the two heaps size , such that difference is not more than one.
    '''    
    if len(min_heap) > len(max_heap) + 1:
        x = min_heap.pop(0)
        max_heap.append(x)
        heapq.heapify(min_heap)
        heapq._heapify_max(max_heap)
    elif len(max_heap) > len(min_heap) + 1:
        x = max_heap.pop(0)
        min_heap.append(x)
        heapq.heapify(min_heap)
        heapq._heapify_max(max_heap)
    
def getMedian():
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :return: return the median of the data received till now.
    '''
    if len(min_heap) == len(max_heap):
        return (min_heap[0] + max_heap[0]) // 2
    elif len(min_heap) > len(max_heap):
        return min_heap[0]
    else:
        return max_heap[0]
    
def insertHeaps(x):
    '''
    use globals min_heap and max_heap, as per declared in driver code
    use heapify modules , already imported by driver code
    :param x: value to be inserted
    :return: None
    '''
    if len(min_heap) == 0 or x > min_heap[0]:
        min_heap.append(x)
        heapq.heapify(min_heap)
    else:
        max_heap.append(x)
        heapq._heapify_max(max_heap)


#{ 
#  Driver Code Starts
#Initial Template for Python 3

import atexit
import io
import sys
import heapq
from collections import  defaultdict

# Contributed by : Nagendra Jha

min_heap = [] # our min heap to be used for upper half of data.
max_heap = [] # our max heap to be used for lower half of data.

if __name__ == '__main__':
    t = int(input())
    
    for _ in range(t):
        n = int(input())
        for i in range(n):
            insertHeaps(int(input()))
            # call this function to balance the two heaps, such that
            # their size does not differ by more than 1.
            balanceHeaps()
            # prints the median
            print(getMedian())

# } Driver Code Ends