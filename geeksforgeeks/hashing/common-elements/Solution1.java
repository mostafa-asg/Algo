// { Driver Code Starts
//Initial Template for Java

/*package whatever //do not write package name here */

import java.io.*;
import java.util.*;
class Solution1 {
    public static void main (String[] args) {
        //taking input using Scanner class
        Scanner sc = new Scanner(System.in);

        //taking total count of testcases
        int t=sc.nextInt();
        while(t-->0)
        {
            //taking total count-1 of elements
            int n=sc.nextInt();

            //Declaring and Initializing an ArrayList-1
            ArrayList<Integer>v1=new ArrayList<>();

            //adding elements to the ArrayList-1
            for(int i=0;i<n;i++)
            {
                v1.add(sc.nextInt());
            }

            //taking total count-2 of elements
            int m=sc.nextInt();

            //Declaring and Initializing an ArrayList-2
            ArrayList<Integer>v2=new ArrayList<>();

            //adding elements to the ArrayList-2
            for(int i=0;i<m;i++)
            {
                v2.add(sc.nextInt());
            }

            //calling the method common_element
            //and passing ArrayList 1, 2 as arguments
            //and storing the results in a new ArrayList
            ArrayList<Integer>ans=common_element(v1, v2);

            //printing the elements of the new ArrayList
            for(int i:ans)
                System.out.print(i+" ");

            System.out.println();
        }
    }


    // } Driver Code Ends


//User function Template for Java

    public static ArrayList<Integer> common_element(ArrayList<Integer>v1, ArrayList<Integer>v2)
    {
        ArrayList<Integer> result = new ArrayList<>();
        HashMap<Integer, Integer> hashV1 = new HashMap<>();
        HashMap<Integer, Integer> hashV2 = new HashMap<>();

        for(Integer num: v1) {
            Integer prevValue = hashV1.getOrDefault(num, 0);
            hashV1.put(num, prevValue + 1);
        }

        for(Integer num: v2) {
            Integer prevValue = hashV2.getOrDefault(num, 0);
            hashV2.put(num, prevValue + 1);
        }

        Set<Integer> keySet1 = hashV1.keySet();
        Set<Integer> keySet2 = hashV2.keySet();

        for (Integer num: keySet1) {
            if (keySet2.contains(num)) {
                Integer count1 = hashV1.get(num);
                Integer count2 = hashV2.get(num);
                Integer mustAppear = (count1 < count2) ? count1 : count2;
                for (int i = 1; i <= mustAppear; i++) {
                    addToSortedList(result, num);
                }
            }
        }

        return  result;
    }

    private static void addToSortedList(ArrayList<Integer> list, Integer num) {
        if (list.isEmpty()) {
            list.add(num);
        } else {
            Integer currentIndex = list.size() - 1;

            while (currentIndex >= 0 && num < list.get(currentIndex)) {
                currentIndex--;
            }

            if (currentIndex < 0) {
                list.add(0, num);
            }
            else {
                if (num < list.get(currentIndex))
                    list.add(currentIndex, num);
                else
                    list.add(currentIndex+1, num);
            }
        }
    }


// { Driver Code Starts.

}  // } Driver Code Ends