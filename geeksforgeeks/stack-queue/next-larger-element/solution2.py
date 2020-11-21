#User function Template for python3
'''
Function Arguments : 
		@param  : arr(given array), n(size of array)
		@return : An array of length n denoting the next greater elements 
		          for all the array elements
'''
def nextLargerElement(arr,n):
    stack = []
    mapping = dict()

    for item in arr:
        if len(stack) == 0:
            stack.append(item)
        else:
            last_item = stack[-1]
            if item < last_item:
                stack.append(item)
            else:
                while item > last_item:
                    mapping[last_item] = item
                    stack.pop()

                    if len(stack) == 0:
                        break

                    last_item = stack[-1]
                stack.append(item)

    return [mapping.get(item, -1) for item in arr]





#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

_INPUT_LINES = sys.stdin.read().splitlines()
input = iter(_INPUT_LINES).__next__
_OUTPUT_BUFFER = io.StringIO()
sys.stdout = _OUTPUT_BUFFER

@atexit.register

def write():
    sys.__stdout__.write(_OUTPUT_BUFFER.getvalue())

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())

        a = list(map(int,input().strip().split()))
        res = nextLargerElement(a,n)
        for i in range (len (res)):
            print (res[i], end = " ")
        print ()
# } Driver Code Ends