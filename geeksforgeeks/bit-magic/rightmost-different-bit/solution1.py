#{ 
#Driver Code Starts
#Initial Template for Python 3

import math




    
 # } Driver Code Ends

#User function Template for python3

##Complete this function
def posOfRightMostDiffBit(m,n):
    pos = 0

    while m>0 and n>0:
        m, rem_m = divmod(m,2)
        n, rem_n = divmod(n,2)

        if rem_m != rem_n:
            return pos + 1

        pos += 1

    if m > 0:
        k = m
    else:
        k = n

    while k > 0:
        k, rem_k = divmod(k,2)

        if rem_k != 0:
            return pos + 1

        pos += 1

    return -1
    


#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        mn=[int(x) for x in input().strip().split()]
        m=mn[0]
        n=mn[1]
        
        print(math.floor(posOfRightMostDiffBit(m,n)))
        
        
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends