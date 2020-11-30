#User function Template for python3

'''
class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
'''

def maxChainLen(pair_list, n):
    pair_list = sorted(pair_list, key=lambda p: p.b)
    counter = 0
    last_b = pair_list[0].b

    for i in range(1, len(pair_list)):
        pair = pair_list[i]
        if last_b < pair.a:
            counter += 1
            last_b = pair.b

    return counter+1

#{ 
#  Driver Code Starts
#Initial Template for Python 3

class Pair(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

if __name__ =='__main__':
    tcs = int(input())

    for _ in range(tcs):
        n=int(input())

        arr=[int(x) for x in input().split()]

        Parr=[]

        i=0
        while n*2>i:

            Parr.append(Pair(arr[i],arr[i+1]))

            i+=2

        #print(Parr,len(Parr))

        print(maxChainLen(Parr, n))
# } Driver Code Ends