using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


public class Solution
{

    /*
        * Problem: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/
        * Time Taken: 
        * Extra Challenge: Could you do it without extra space and in O(n) runtime? 
        * You may assume the returned list does not count as extra space.
        */

    public IList<int> swapMethod(int[] nums)
    {
        /* Idea: Swap the numbers to their correct position. Because each swap garuntees a number in
        * the correct position, it should be O(n). Swap is also in place. 
        * Ex: [4,3,2,7,8,2,3,1]
        * [7,3,2,4,8,2,3,1]
        * [3,3,2,4,8,2,7,1]
        * [2,3,3,4,8,2,7,1]
        * [3,2,3,4,8,2,7,1]
        * [0,2,3,4,8,2,7,1]
        * [0,2,3,4,1,2,7,8]
        * [1,2,3,4,0,0,7,8]
        */

        for (int index = 0; index < nums.Length; index++)
        {
            while (nums[index] != index+1 && nums[index] != 0)
            {
                if (nums[index] == nums[nums[index]-1])
                {
                    nums[index] = 0;
                }
                else
                {
                    int temp = nums[index];
                    nums[index] = nums[nums[index] - 1];
                    nums[temp - 1] = temp;
                }
                //nums.ToList().ForEach(Console.Write);
                //Console.WriteLine();
            }
        }

        IList<int> result = new List<int>();
        for (int index = 0; index < nums.Length; index++)
        {
            if (nums[index] == 0)
            {
                result.Add(index + 1);
            }
        }

        return result;
    }

    public IList<int> FindDisappearedNumbers(int[] nums)
    {
        return swapMethod(nums);
    }


    public static void Main(string[] args)
    {
        Solution test = new Solution();
        IList<int> result = test.FindDisappearedNumbers(new[] {1, 1});
        foreach(int i in result)
        {
            Console.Write(i);
        }
        Console.ReadLine();
    }
}