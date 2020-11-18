import heapq

#User function Template for python3
def maximumActivities(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    sorted_time = sorted(start)
    scheduler = []

    # Add activities to the scheduler
    for s_time, e_time in zip(start, end):
        heapq.heappush(scheduler, (s_time + (e_time-s_time), (s_time, e_time)))

    done_tasks = 0
    missed_tasks = 0
    current_time = sorted_time[0]

    for _ in sorted_time:
        first_task_to_be_executed = scheduler[0]
        s_time, e_time = first_task_to_be_executed[1]

        if current_time <= s_time:
            done_tasks = done_tasks + 1            
            current_time = e_time
        else:
            missed_tasks = missed_tasks + 1

        heapq.heappop(scheduler)

    return done_tasks

        

#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for cases in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        print(maximumActivities(n,start,end))
# } Driver Code Ends