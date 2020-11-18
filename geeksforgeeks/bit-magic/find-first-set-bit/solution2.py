#{ 
#Driver Code Starts
#Initial Template for Python 3

import math



 # } Driver Code Ends

#User function Template for python3

##Complete this function
def getFirstSetBit(n):
    counter = 0
    while n > 0:
        n, rem = divmod(n, 2)
        if rem == 1:
            return counter + 1

        counter = counter + 1

    return 0


#{ 
#Driver Code Starts.
    
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        n=int(input())
        
        print(getFirstSetBit(n))
        
        
        T-=1
    
    




if __name__=="__main__":
    main()
#} Driver Code Ends