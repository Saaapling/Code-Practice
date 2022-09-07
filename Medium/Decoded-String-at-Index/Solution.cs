using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

public class Solution
{

    /*
        Problem: https://leetcode.com/problems/decoded-string-at-index/
        Time Taken: 75 min
        Comments: While the 2nd solution works and is similiar to the posted solution, the better method (posted solution)
            is to work backwards instead of forwards, removing the time needed to reprocess already seen parts of the string

        Posted solution (C++):
            string decodeAtIndex(string S, int K) {
            long size = 0;
            int N = S.size();

            // Find size = length of decoded string
            for (int i = 0; i < N; ++i) {
                if (isdigit(S[i]))
                    size *= S[i] - '0';
                else
                    size++;
            }

            for (int i = N-1; i >=0; --i) {
                K %= size;
                if (K == 0 && isalpha(S[i]))
                    return (string) "" + S[i];

                if (isdigit(S[i]))
                    size /= S[i] - '0';
                else
                    size--;
            }
            return "";
    }

    */

    public string naive_solution(string s, int k)
    {
        StringBuilder current = new StringBuilder();
        int index = 0;
        foreach (char x in s)
        {
            if (Char.IsNumber(x))
            {
                int iterations = (int)(Char.GetNumericValue(x) - 1);
                string temp = current.ToString();
                for (int i = 0; i < iterations; i++)
                {
                    current.Append(temp);
                }
                index *= (iterations + 1);
            }
            else
            {
                current.Append(x);
                index++;
            }

            if (index >= k)
            {
                return current.ToString()[k - 1].ToString();
            }
        }

        return "";
    }


    public string recursive_solution(string s, int k)
    {
        long index = 0;
        char last_char = ' ';
        for (int i = 0; i < s.Length; i++)
        {
            char x = s[i];
            if (Char.IsNumber(x))
            {
                long iterations = (long) (Char.GetNumericValue(x) - 1);
                if (index * (iterations + 1f) >= k)
                {
                    int new_k = (int)(k % index);
                    //Console.WriteLine(index);
                    //Console.WriteLine(s.Substring(0, i));
                    //Console.WriteLine(new_k);
                    if (new_k == 0)
                    {
                        return last_char.ToString();
                    }
                    return recursive_solution(s.Substring(0, i), new_k);
                }
                index *= (iterations + 1);
            }
            else
            {
                if (index == k - 1)
                {
                    return x.ToString();
                }
                last_char = x;
                index++;
            }
        }

        return "Error";
    }

    public string DecodeAtIndex(string s, int k)
    {
        return recursive_solution(s, k);
    }

    static void Main(string[] args)
    {
        Solution test = new Solution();
        string result = test.DecodeAtIndex("ajx37nyx97niysdrzice4petvcvmcgqn282zicpbx6okybw93vhk782unctdbgmcjmbqn25rorktmu5ig2qn2y4xagtru2nehmsp", 976159153);
        Console.WriteLine(result);
        Console.ReadKey();
    }
}