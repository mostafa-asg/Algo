#User function Template for python3

def Push(x,inbox,outbox):
    '''
    x: value to push
    stack1: list
    stack2: list
    '''
    inbox.append(x)
    
    

def Pop(inbox,outbox):    
    '''
    stack1: list
    stack2: list
    '''
    if len(outbox) == 0:
        while len(inbox) > 0:
            item = inbox.pop()
            outbox.append(item)

    if len(outbox) == 0:
        return -1
    else:
        return outbox.pop()
        



#{ 
#  Driver Code Starts
#Initial Template for Python 3

#contributed by RavinderSinghPB
if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases):
        qry=int(input())
        qtyp_qry=list(map(int, input().strip().split()))
        
        i=0
        stack1=[]
        stack2=[]
        while i <len(qtyp_qry):
            #print(i)
            if qtyp_qry[i]==1:
                Push(qtyp_qry[i+1],stack1,stack2)
                #print(i)
                i+=2
            else:
                print(Pop(stack1,stack2),end=' ')
                i+=1
                
        print()
# } Driver Code Ends