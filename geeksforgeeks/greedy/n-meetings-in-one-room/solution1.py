from collections import namedtuple

Meeting = namedtuple("Meeting", "end index start")


#User function Template for python3
def maximumMeetings(n,start,end):
    '''
    :param n: number of activities
    :param start: start time of activities
    :param end: corresponding end time of activities
    :return: Integer, maximum number of activities
    '''
    meeting_list = []
    for i in range(len(start)):
        meeting_list.append(Meeting(end[i], i+1, start[i]))

    meeting_list = sorted(meeting_list)

    t = -1
    for meeting in meeting_list:
        if meeting.start > t:
            print(meeting.index, end=" ")
            t = meeting.end 
    print("")





#{ 
#  Driver Code Starts
#Initial Template for Python 3
import atexit
import io
import sys

#Contributed by : Nagendra Jha

if __name__ == '__main__':
    test_cases = int(input())
    for caes in range(test_cases) :
        n = int(input())
        start = list(map(int,input().strip().split()))
        end = list(map(int,input().strip().split()))
        maximumMeetings(n,start,end)
# } Driver Code Ends