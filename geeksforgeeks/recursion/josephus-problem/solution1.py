#{ 
#Driver Code Starts
import math



 # } Driver Code Ends

#Complete this function
def josephus(n,k):
    alive = {i for i in range(0,n)}
    circle = [1 for i in range(0,n)] # 1 is alive, 0 is dead

    pos = -1

    while len(alive) > 1:
        pos = skip(pos, circle, k-1)

        # kill
        circle[pos] = 0
        alive.remove(pos)

    return alive.pop() + 1 # 1-based indexes


def skip(pos, circle, how_many):
    skipped = 0
    how_many += 1

    while skipped < how_many:
        pos += 1
        if pos >= len(circle):
            pos = 0

        if circle[pos] == 1:
            skipped += 1

    return pos


#{ 
#Driver Code Starts.
    
def main():
    
    T=int(input())
    
    while(T>0):
        
        
        nk=[int(x) for x in input().strip().split()]
        n=nk[0]
        k=nk[1]
        
        print(josephus(n,k))
        
        T-=1

if __name__=="__main__":
    main()
#} Driver Code Ends