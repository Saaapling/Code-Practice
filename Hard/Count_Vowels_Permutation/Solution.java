package Hard.Count_Vowels_Permutation;

public class Solution {

    /**
     * Problem: https://leetcode.com/problems/count-vowels-permutation/
     * Time Taken: 15 min (initial solution)
     * Comments:
     *      - Feels like a dynamic programming problem
     *          - Keep a list possible permutations of length 'n' that end with 'a', 'e', etc.
     *          - Calculate this list for 'n+1'
     *      - Also feels like there is likely to be a pattern for this
     *          - The array will definitely overflow, need a solution for that
     *          - The solution will be modulo 10^9 + 7
     *      - Post submission:
     *          - Initial solution is somewhat slow, but correct
     *          - Doesn't feel like a 'hard' problem compared to the other 'hard' DP questions
     *          - Improved solution: Same format, but without saving all the previous results. Since
     *                  we only care about (n-1) to calculate n, we can discard everything before n-1,
     *                  and use 2 int[5] arrays instead of the entire int[n][5]. This greatly improves
     *                  both runtime and memory usage.
    */

    public int countVowelPermutation_improved(int n) {
        int modulo = (int) (Math.pow(10,9) + 7);
        int[] permutations = {1,1,1,1,1};

        for (int i = 2; i <= n; i++){
            int[] temp = new int[5];
            temp[0] = ((permutations[1] + permutations[2]) % modulo + permutations[4]) % modulo;
            temp[1] = (permutations[0] + permutations[2]) % modulo;
            temp[2] = (permutations[1] + permutations[3]) % modulo;
            temp[3] = (permutations[2]) % modulo;
            temp[4] = (permutations[2] + permutations[3]) % modulo;
            permutations = temp;
        }

        int sum = 0;
        for (int i = 0; i < 5; i++){
            sum += permutations[i];
            sum %= modulo;
        }

        return sum;
    }

    public int countVowelPermutation(int n) {
        int modulo = (int) (Math.pow(10,9) + 7);
        long[][] permutations = new long[n+1][5];
        permutations[1] = new long[]{1,1,1,1,1};

        for (int i = 2; i <= n; i++){
            permutations[i][0] = (permutations[i-1][1] + permutations[i-1][2] + permutations[i-1][4]) % modulo;
            permutations[i][1] = (permutations[i-1][0] + permutations[i-1][2]) % modulo;
            permutations[i][2] = (permutations[i-1][1] + permutations[i-1][3]) % modulo;
            permutations[i][3] = (permutations[i-1][2]) % modulo;
            permutations[i][4] = (permutations[i-1][2] + permutations[i-1][3]) % modulo;
        }

        long sum = 0;
        for (int i = 0; i < 5; i++){
            sum += permutations[n][i];
            sum %= modulo;
        }

        return (int) sum;
    }

    public static void main(String[]args){
        Solution test = new Solution();
        System.out.println(test.countVowelPermutation((int) Math.pow(10,4)));
        System.out.println(test.countVowelPermutation_improved((int) Math.pow(10,4)));
    }
}
