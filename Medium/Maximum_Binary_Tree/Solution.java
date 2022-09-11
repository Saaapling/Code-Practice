package Medium.Maximum_Binary_Tree;

import com.sun.source.tree.Tree;

import java.util.*;

public class Solution {

    /**
     * Problem: https://leetcode.com/problems/maximum-binary-tree/
     * Initial Time Taken: 10 minutes (naive method)
     * Improved Version: There is an O(n) solution that builds the tree as it goes through the array.
     *      This solution was provided in C++ and converted to Java.
     * Improved Version Implementation: 20 (understanding the method) + 15 (implementation)
     * Comments: I tried using both a Deque and a Stack. Not sure if the Stack implementation is the most
     *      efficient. Both the deque and the stack performed worse than the naive method of leetcode,
     *      but I assume for large testcases, the O(N) complexity should be an improvement over the O(N^2)
     *      of the naive method
     */

    // Provided by the problem
    public class TreeNode {
        int val;
        TreeNode left;
        TreeNode right;
        TreeNode() {}
        TreeNode(int val) { this.val = val; }
        TreeNode(int val, TreeNode left, TreeNode right) {
            this.val = val;
            this.left = left;
            this.right = right;
        }

        public ArrayList<Integer> get_values(){
            ArrayList<Integer> left_vals = new ArrayList<>();
            ArrayList<Integer> right_vals = new ArrayList<>();
            if (left != null){
                left_vals = left.get_values();
            }
            if (right != null){
                right_vals = right.get_values();
            }

            ArrayList<Integer> values = new ArrayList();
            values.add(val);
            values.addAll(left_vals);
            values.addAll(right_vals);

            return values;
        }

        public void print_tree(){
            ArrayList<Integer> values = get_values();
            System.out.println(values.toString());
        }
    }

    public TreeNode naive_recursive_solution(int[] nums){
        // Break recursion
        if (nums.length == 0){
            return null;
        }else if (nums.length == 1){
            return new TreeNode(nums[0]);
        }

        // Get largest element
        int max = 0;
        int index = 0;
        for (int i = 0; i < nums.length; i++){
            if (nums[i] > max){
                index = i;
                max = nums[i];
            }
        }

        // Separate array and recurse
        int[] left = Arrays.copyOfRange(nums, 0, index);
        int[] right = Arrays.copyOfRange(nums, index + 1, nums.length);
        TreeNode left_tree = naive_recursive_solution(left);
        TreeNode right_tree = naive_recursive_solution(right);

        // Combine results
        TreeNode result = new TreeNode(nums[index], left_tree, right_tree);

        return result;
    }

    public TreeNode big_brain_solution(int[] nums){
        Stack<TreeNode> values_queue = new Stack<>();
        for (int value : nums){
            TreeNode curr = new TreeNode(value);
            while (!values_queue.isEmpty() && values_queue.peek().val < value){
                curr.left = values_queue.pop();
            }
            if (!values_queue.isEmpty()){
                values_queue.peek().right = curr;
            }

            values_queue.add(curr);
        }

        return values_queue.firstElement();
    }

    public TreeNode constructMaximumBinaryTree(int[] nums) {
        return big_brain_solution(nums);
    }

    public static void main(String[]args){
        Solution test = new Solution();
        int[] input = {3,2,1,6,0,5};
        TreeNode result = test.constructMaximumBinaryTree(input);
        System.out.println(result.right.val);
    }
}
