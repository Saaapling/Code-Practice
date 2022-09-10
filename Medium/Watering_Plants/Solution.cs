using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class Solution
{
    /*
    * Problem: https://leetcode.com/problems/watering-plants/
    * Time Taken: 7 min
    */

    public int naive_solution(int[] plants, int capacity)
    {
        int current = capacity;
        int steps = 0;
        
        for (int index = 0; index < plants.Length; index++)
        {
            // Check if you water the plant
            if (plants[index] > current)
            {
                // Walk to the river, and then back to the original position
                steps += index * 2;
                current = capacity;
            }

            // Walk to the plant
            steps++;

            // Water the plant
            current -= plants[index];
        }

        return steps;
    }

    public int WateringPlants(int[] plants, int capacity)
    {
        return naive_solution(plants, capacity);
    }

    public static void Main(string[] args)
    {
        Solution test = new Solution();
        int[] plants = { 7, 7, 7, 7, 7, 7, 7 };
        int capacity = 8;

        int result = test.WateringPlants(plants, capacity);
        Console.WriteLine(result);
        Console.ReadLine();
    }
}
