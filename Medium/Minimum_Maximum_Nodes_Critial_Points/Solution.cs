using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice_Code.Minimum_Maximum_Nodes_Critial_Points
{
    internal class Solution
    {

        /*
         * Problem: https://leetcode.com/problems/find-the-minimum-and-maximum-number-of-nodes-between-critical-points/
         * Time Taken: ~15-30 min (had to leave mid-problem, and came back to finish)
         * Comments: The method should be correct, space complexity is good, time is not great, but its more of a runtime
         *      randomness / variability than being really inefficient (300+ ms swings with the same code)
         *      - Need to get use to writing own test cases, even for problems with slightly annoying setup like this one
         *      - Many many small bugs when submitting without testing
         */


        public class ListNode {
            public int val;
            public ListNode next;

            public ListNode(int val=0, ListNode next=null) {
                this.val = val;
                this.next = next;
            }

            public ListNode(int[] values)
            {
                val = values[0];
                ListNode curr = this;
                for (int i = 1; i < values.Length; i++)
                {
                    ListNode new_node =  new ListNode(values[i]);
                    curr.next = new_node;
                    curr = curr.next;
                }
            }
        }

        public int[] NodesBetweenCriticalPoints_improved(ListNode head)
        {
            if (head.next == null || head.next.next == null)
                return new int[] { -1, -1 };

            int i = head.val;
            int j = head.next.val;
            head = head.next.next;

            int first = -1;
            int last = -1;
            int min = int.MaxValue;
            int index = 0;
            while (head != null)
            {
                int k = head.val;
                // Critical Point: Max/Min
                if ((i < j && k < j) || (i > j && k > j))
                {
                    if (first < 0)
                        first = index;
                    else
                        if (index - last < min)
                            min = index - last;
                    last = index;
                }
                i = j;
                j = k;
                index++;
                head = head.next;
            }

            if (first == last)
                return new int[] { -1, -1 };

            return new int[] { min, last - first };
        }

        public int[] NodesBetweenCriticalPoints(ListNode head)
        {
            List<int> critical_points = new List<int>();

            int i = head.val;
            if (head.next == null)
                return new int[] { -1, -1 };
            head = head.next;

            int j = head.val;
            if (head.next == null)
                return new int[] { -1, -1 };
            head = head.next;

            int index = 1;
            while (head != null)
            {
                int k = head.val;
                // Critical Point: Max/Min
                if ((i < j && k < j) || (i > j && k > j))
                {
                    critical_points.Add(index);
                }
                i = j;
                j = k;
                index++;
                head = head.next;
            }

            if (critical_points.Count < 2)
                return new int[] { -1, -1 };

            int min = int.MaxValue;
            for (i = 1; i < critical_points.Count; i++)
            {
                if (critical_points[i] - critical_points[i-1] < min)
                {
                    min = critical_points[i] - critical_points[i - 1];
                }
            }
            int max = critical_points[critical_points.Count - 1] - critical_points[0];

            return new int[] { min, max };
        }

        public static void Main(string[] args)
        {
            Solution solution = new Solution();
            int[] input = {1, 3, 2, 2, 3, 2, 2, 2, 7};
            ListNode list = new ListNode(input);
            int[] result = solution.NodesBetweenCriticalPoints_improved(list);
            Console.WriteLine(result[0]);
            Console.WriteLine(result[1]);
            Console.ReadKey();
        }
    }
}
