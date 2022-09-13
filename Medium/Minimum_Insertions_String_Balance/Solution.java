package Medium.Minimum_Insertions_String_Balance;

import java.util.Stack;

public class Solution {

    /**
     * Problem: https://leetcode.com/problems/minimum-insertions-to-balance-a-parentheses-string/
     * Time Taken: 23 minutes
     * Comments:
     *      Solution 1: Keep a stack of previous inputs, take action based on next input
     *              - '(' :
     *                  - If the previous option was an '(', do nothing
     *                  - If previous value was ')', add an extra ')' to the stack and resolve it
     *                  - If the stack is empty, do nothing
     *              - ')' :
     *                  - If the previous option was an '(', do nothing
     *                  - If the previous option was an ')', resolve the stack
     *                  - If the stack is empty, add an extra '(' prior to this entry
     *          - The stack will never have more than one ')', as once there are two ')'s, the stack
     *              is resolved
     *          - Post submission comments: This method is apparently very slow...
     *                  - Improvement 1: Simply operations by removing 'unneeded' stack operations (Minor Improvement)
     *                  - Improvement 2: Replace the stack with a last_char tracker and an int representing the number
     *                          of open parenthesis. This works because at any state, the stack is a series of '('s
     *                          followed by at most 1 ')'. (Major improvement)
     */

    public int minInsertions3(String s) {
        char last = ' ';
        int insertions = 0;
        int open = 0;

        for (char x : s.toCharArray()){
            if (x == '('){
                if (last == ')'){
                    insertions += 1;
                }else{
                    open += 1;
                }
                last = '(';
            }else{
                if (last == ' '){
                    open = 1;
                    insertions += 1;
                    last = ')';
                }else if (last == '(') {
                    last = ')';
                }else{
                    open -= 1;
                    if (open == 0)
                        last = ' ';
                    else
                        last = '(';
                }
            }
        }

        if (open > 0){
            if (last == '('){
                insertions += 2*open;
            }else{
                insertions += 1 + 2*(open-1);
            }
        }

        return insertions;
    }

    public int minInsertions2(String s) {
        Stack<Character> stack = new Stack<>();

        int insertions = 0;
        for (char x : s.toCharArray()){
            if (x == '('){
                if (!stack.empty()){
                    if (stack.peek() == ')'){
                        insertions += 1;
                        stack.pop();
                        stack.pop();
                    }
                }
                stack.add(x);
            }else{
                if (stack.empty()){
                    insertions += 1;
                    stack.add('(');
                    stack.add(x);
                }else{
                    if (stack.peek() == '('){
                        stack.add(x);
                    }else{
                        stack.pop();
                        stack.pop();
                    }
                }
            }
        }

        if (!stack.isEmpty()){
            if (stack.pop() == ')') {
                insertions += 1;
                stack.pop();
            }else
                insertions += 2;
            insertions += stack.size() * 2;
        }

        return insertions;
    }

    public int minInsertions(String s) {
        Stack<Character> stack = new Stack<>();

        int insertions = 0;
        for (char x : s.toCharArray()){
            if (x == '('){
                if (stack.empty()){
                    stack.add(x);
                }else{
                    char y = stack.peek();
                    if (y == '('){
                        stack.add(x);
                    }else{
                        // Add a missing ')', then remove a completed pair
                        insertions += 1;
                        stack.pop();
                        stack.pop();
                        stack.add(x);
                    }
                }
            }else{
                if (stack.empty()){
                    insertions += 1;
                    stack.add('(');
                    stack.add(x);
                }else{
                    char y = stack.peek();
                    if (y == '('){
                        stack.add(x);
                    }else{
                        // Remove a completed pair
                        stack.pop();
                        stack.pop();
                    }
                }
            }
        }

        if (!stack.isEmpty()){
            if (stack.pop() == ')') {
                // Insert an extra ')' and remove a completed pair
                insertions += 1;
                stack.pop();
            }else
                // Insert 2 extra ')'s
                insertions += 2;
            // Add 2 extra ')'s for every '(' remaining in the stack
            insertions += stack.size() * 2;
        }

        return insertions;
    }

    public static void main(String[]args){
        Solution test = new Solution();
        String input = "())";
        int result = test.minInsertions3(input);
        System.out.println(result);
    }
}
