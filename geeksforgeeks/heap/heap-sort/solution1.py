#User function Template for python3
def heapify(arr, n, i):
    '''
    :param arr: original array
    :param n: size of original array
    :param i: subtree rooted at ith index
    :return: 
    '''
    left_index = i*2+1
    right_index = i*2+2
    max_index = i

    if left_index < n and arr[left_index] > arr[i]:
        max_index = left_index

    if right_index < n and arr[right_index] > arr[max_index]:
        max_index = right_index

    if max_index != i:
        # swap
        arr[i], arr[max_index] = arr[max_index], arr[i]
        heapify(arr, n, max_index)

def buildHeap(arr,n):
    '''
    :param arr: given array
    :param n: size of array
    :return: None
    '''
    for i in range(n//2-1, -1, -1):
        heapify(arr, n, i)

    for i in range(n-1, 0, -1):
        # swap
        arr[0], arr[i] = arr[i], arr[0]
        heapify(arr, i, 0)




#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

# Contributed by : Mohit Kumara

if __name__ == '__main__':
    # test_cases = int(input())
    # for cases in range(test_cases):
    #     n = int(input())
    #     arr = list(map(int, input().strip().split()))
    arr = [4, 1, 3, 9, 7]
    buildHeap(arr,len(arr))
    print(*arr)

# } Driver Code Ends