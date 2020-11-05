Given an input stream of N integers. The task is to insert these numbers into a new stream and find the median of the stream formed by each insertion of X to the new stream.

## Example 1:

### Input:
N = 4
X[] = 5,15,1,3
### Output:
5
10
5
4
### Explanation:Flow in stream : 5, 15, 1, 3 
5 goes to stream --> median 5 (5)   
15 goes to stream --> median 10 (5,15)   
1 goes to stream --> median 5 (5,15,1)    
3 goes to stream --> median 4 (5,15,1 3)   
Your Task:  
You are required to complete 3 methods insertHeap() which takes 1 argument,   balanceHeaps() and getMedian() and returns the current median.  
### Expected Time Complexity : O(nlogn)
### Expected Auxilliary Space : O(n)
 
## Constraints:
1 <= N <= 106  
1 <= x <= 106  

## Original link
https://practice.geeksforgeeks.org/problems/find-median-in-a-stream-1587115620/1#