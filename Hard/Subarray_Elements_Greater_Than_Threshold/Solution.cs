using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Practice_Code.Subarray_Elements_Greater_Than_Threshold
{
    class SegmentTree
    {
        int n;
        int[] values;

        public SegmentTree(int n)
        {
            this.n = n;
            values = new int[n * 2];
        }

        public int get(int x)
        {
            return values[x + n];
        }

        public int get_maximum(int start, int end)
        {
            int low = start + n;
            int high = end + n;
            int max = 0;
            while (low <= high)
            {
                if (low % 2 == 1)
                {
                    max = Math.Max(max, values[low]);
                    low++;
                }
                if (high % 2 == 0)
                {
                    max = Math.Max(max, values[high]);
                    high--;
                }
                low >>= 1;
                high >>= 1;
            }

            return max;
        }

        public void update(int index, int value)
        {
            index += n;
            while (index > 0 && value > values[index])
            {
                values[index] = value;
                index >>= 1;
            }
        }

        public int segtree_attempt(int[] nums, int threshold)
        {
            SegmentTree tree = new SegmentTree(nums.Length);

            for (int i = 0; i < nums.Length; i++)
            {
                int value = (int)Math.Floor((double)threshold / nums[i]) + 1;
                tree.update(i, value);
            }

            for (int i = 0; i < nums.Length; i++)
            {
                int size = tree.get(i);
                if (i + size - 1 >= nums.Length)
                    continue;
                if (tree.get_maximum(i, i + size - 1) <= size)
                {
                    return size;
                }
            }

            return -1;
        }
    }

    class Solution
    {
        /*
         * Problem: https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/
         * Time Taken: ad-ifinitum :/
         * Comments: 
         *      Initial Soluton: Array iteration with Segment Tree lookup
         *          - This doesn't work the way its implemented
         *          - The key part is that the method does a forward-only search
         *              - num[i] with k = threshold / nums[i] will search the seg-tree on start = i, end = i + k
         *              - This means each index searches for 1-valid subarray with which it is the starting index, but this isn't actually valid
         *              - input = [7,1,1,1], threshold = 9 has a valid solution of 3 that starts with i=0, but this method won't find it
         *      Actual Solution: Use a monotonically increasing stack:
         *          - Reference: https://leetcode.com/problems/subarray-with-elements-greater-than-varying-threshold/discuss/2346947/Java-or-Easy-To-Understand-or-Monotonic-Stack-or-O(N)-Time-or-O(N)-Space
         *          - The idea is that when an element is added to the stack, all elements prior that are greater
         *              than it are removed, making that element the new 'largest' element in the stack. Removed
         *              elements are then checked for subsequence viability
         *          - Source of confusion: How does a monotonically increasing stubsstack function when elements greater
         *              than it are removed? It works because the new element *must* be placed in the stack, and
         *              pervious elements are still factored in calculations since subsequence checks use the last
         *              two indexes in the stack
         *          - When an element is popped from the stack, it is the smallest of its subsequence because:
         *              - Elements larger than it have already been added to the stack and subsequently popped
         *              - The first element smaller than it will pop this element from the stack, thus it remains
         *                  the smallest up to the element that popped it
         */


        public int ValidSubarraySize(int[] nums, int threshold)
        {
            Stack<int> value_stack = new Stack<int>();
            Stack<int> index_stack = new Stack<int>();
            for (int i = 0; i < nums.Length; i++)
            {
                int index = i;
                while (value_stack.Count > 0 && value_stack.Peek() > nums[i])
                {
                    
                    index = index_stack.Pop();
                    int length = i - index;
                    if ((double) (threshold) / length < value_stack.Pop()) {
                        return length;
                    }
                }

                value_stack.Push(nums[i]);
                index_stack.Push(index);
            }

            while (value_stack.Count > 0)
            {
                int index = index_stack.Pop();
                int length = nums.Length - index;
                if ((double)(threshold) / length < value_stack.Pop())
                {
                    return length;
                }
            }

            return -1;
        }

        public static void Main(string[] args)
        {
            Solution test = new Solution();
            int[] large_input = { 802004, 526012, 757957, 243310, 336124, 392107, 848457, 803125, 717278, 852486, 610801, 759260, 72807, 829109, 541803, 636250, 444453, 580149, 868656, 927123, 474186, 354523, 264432, 502901, 404597, 712395, 414671, 370171, 844118, 436342, 814834, 223136, 241147, 628114, 50190, 303165, 21529, 380855, 415102, 665756, 609251, 839401, 147755, 69452, 843840, 913447, 732169, 49180, 511772, 713914, 201539, 60494, 461204, 568364, 702691, 319442, 922352, 184092, 243907, 968459, 143049, 718846, 182837, 861363, 860650, 968638, 801282, 516775, 532771, 647870, 409083, 791685, 915733, 221261, 508832, 768406, 88418, 884339, 904590, 120156, 363069, 986042, 90171, 390140, 438122, 936681, 926414, 186991, 544691, 799527, 564251, 764831, 214353, 829085, 180620, 397536, 86549, 728013, 659691, 534196, 474616, 882189, 276590, 907311, 654637, 655805, 121256, 868286, 661438, 65951, 829879, 319639, 423120, 57508, 653691, 185627, 573512, 657657, 85111, 118794, 931267, 303261, 52081, 702907, 897650, 574513, 515576, 524929, 274063, 78281, 626052, 127623, 155965, 836595, 781293, 22150, 421308, 803448, 652756, 423612, 509389, 720333, 207593, 950394, 445218, 421491, 34285, 941325, 329057, 182104, 791318, 784413, 563697, 204658, 19810, 319531, 267681, 100503, 773294, 799637, 739396, 956008, 111779, 632934, 167024, 22616, 805292, 834536, 409322, 827234, 147246, 683958, 23887, 524398, 62834, 645434, 890827, 312685, 300035, 296658, 748427, 240125, 862121, 215413, 164406, 662036, 943738, 942985, 620555, 600387 };
            int[] input = new int[18];
            int[] order = new int[18];
            int minimum = 4569796;
            for (int i = 0; i < 18; i++)
            {
                input[i] = large_input[i + 13];
                if (minimum > input[i])
                {
                    minimum = input[i];
                }
                order[i] += 1;
                for (int j = 0; j < i; j++)
                {
                    if (input[j] > input[i])
                    {
                        order[j] += 1;
                    }
                    else{
                        order[i] += 1;
                    }
                }
            }
            int threshold = 4569796;
            Console.WriteLine(threshold / 18);
            Console.WriteLine(minimum);




            int result = test.ValidSubarraySize(input, threshold);
            Console.WriteLine(result);
            Console.ReadLine();
        }
    }
}
