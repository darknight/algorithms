/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode(int x) { val = x; }
 * }
 */
public class Solution {
    
    public List<Integer> inorderTraversal(TreeNode root) {
        if(root == null) return new ArrayList<Integer>();
        List<Integer> res = inorderTraversal(root.left);
        res.add(root.val);
        res.addAll(inorderTraversal(root.right));
        return res;
    }

    public List<Integer> inorderTraversal_2(TreeNode root) {
        Stack<Object> stack = new Stack<Object>();
        List<Integer> res = new ArrayList<Integer>();
        stack.push(root);
        while(!stack.empty()) {
            Object x = stack.pop();
            if(x == null) continue;
            if(x instanceof TreeNode) {
                TreeNode node = (TreeNode)x;
                stack.push(node.right);
                stack.push(node.val);
                stack.push(node.left);
            } else {
                res.add((Integer)x);
            }
        }
        return res;
    }

    public List<Integer> inorderTraversal_3(TreeNode root) {
        Stack<TreeNode> stack = new Stack<TreeNode>();
        List<Integer> res = new ArrayList<Integer>();
        TreeNode current = root;
        while(!stack.empty() || current != null) {
            if(current != null) {
                stack.push(current);
                current = current.left;
            } else {
                TreeNode node = stack.pop();
                res.add(node.val);
                current = node.right;
            }
        }
        return res;
    }
}