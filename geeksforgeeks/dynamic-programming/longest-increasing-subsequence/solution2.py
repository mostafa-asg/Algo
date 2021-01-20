#User function Template for python3

def add_in_sorted_list(lst, item_to_add):
    if item_to_add == 1:
        AAA=111
    list_size = len(lst)

    if list_size == 0:
        lst.append(item_to_add)
        return
    
    if item_to_add > lst[list_size - 1]:
        lst.append(item_to_add)    
        return
    
    count = list_size    
    first = 0
    while count > 0:
        current_index = first
        jump = count // 2
        current_index += jump
        if lst[current_index] < item_to_add:
            first = current_index + 1
            count -= jump + 1
        else:
            count = jump
        
    lst[first] = item_to_add

def longestSubsequence(arr,arr_size):
    lst = []

    for item in arr:        
        add_in_sorted_list(lst, item)        
    
    return len(lst)

    



#{ 
#  Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__':
    for _ in range(int(input())):
        n = int(input())
        a = [ int(x) for x in input().split() ]
        print(longestSubsequence(a,n))
# } Driver Code Ends