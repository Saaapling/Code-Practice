package Medium.Logical_OR_Binary_Grids_as_Quad_Trees;

public class Solution {

    /**
     * Problem: https://leetcode.com/problems/logical-or-of-two-binary-grids-represented-as-quad-trees/
     * Time Taken: 17 min
     * Comments:
     *      - The naive solution is to construct the full array. This obviously is too expensive
     *      - Possibly construct the new tree as the traversal is done (recursion)
     *          - if leaf = 1, copy this leaf over to the result
     *          - if leaf = 0, set the other tree's full subtree/leaf to the result
     * Post-Submission comments:
     *      - The runtime was good, but the memory-usage was poor. But I'm not sure how to improve that
     */

    class Node {
        public boolean val;
        public boolean isLeaf;
        public Node topLeft;
        public Node topRight;
        public Node bottomLeft;
        public Node bottomRight;

        public Node() {}

        public Node(boolean _val,boolean _isLeaf,Node _topLeft,Node _topRight,Node _bottomLeft,Node _bottomRight) {
            val = _val;
            isLeaf = _isLeaf;
            topLeft = _topLeft;
            topRight = _topRight;
            bottomLeft = _bottomLeft;
            bottomRight = _bottomRight;
        }
    };

    public Node recursive_solution(Node tree_a, Node tree_b){
        // Break recursion
        if (tree_a.isLeaf){
            return tree_a.val ? tree_a: tree_b;
        }else if (tree_b.isLeaf){
            return tree_b.val ? tree_b: tree_a;
        }

        Node ul = recursive_solution(tree_a.topLeft, tree_b.topLeft);
        Node ur = recursive_solution(tree_a.topRight, tree_b.topRight);
        Node bl = recursive_solution(tree_a.bottomLeft, tree_b.bottomLeft);
        Node br = recursive_solution(tree_a.bottomRight, tree_b.bottomRight);

        // Consolidate trees (All 0's or 1's)
        if (ul.isLeaf && ur.isLeaf && bl.isLeaf && br.isLeaf){
            if (ul.val == ur.val && ur.val == bl.val && bl.val == br.val){
                return new Node(ul.val, true, null, null, null, null);
            }
        }

        return new Node(false, false, ul, ur, bl, br);
    }

    public Node intersect(Node quadTree1, Node quadTree2) {
        return recursive_solution(quadTree1, quadTree2);
    }

    public static void main(String[]args){
        Solution test = new Solution();
        Node result = test.intersect(null, null);
    }
}
