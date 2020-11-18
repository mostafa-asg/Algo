Given N activities with their start and finish times. Select the maximum number of activities that can be performed by a single person, assuming that a person can only work on a single activity at a time.

**Note** : The start time and end time of two activities may coincide.

## Example 1:

### Input:
N = 5  
start[] = {1,3,2,5,8,5}  
end[] = {2,4,6,7,9,9}  
Output: 4  
Explanation:Perform the activites 1,2,4,5  

## Example 2:
### Input:
N = 4  
start[] = {1,3,2,5}  
end[] = {2,4,3,6}  
Output: 4  
Explanation:Perform the activities1,3,2,4  
Your Task :  
 Complete the function activityselection() that recieves start-time array , end-time array and number of activites as parameters and returns the maximum number of activities that can be done.

## Constraints:
* 1 <= N <= 105
* 1 <= start[i] <= end[i] <= 105
* Expected Time Complexity : O(NlogN)
* Expected Auxilliary Space : O(1)

## Original link
https://practice.geeksforgeeks.org/problems/activity-selection-1587115620/1