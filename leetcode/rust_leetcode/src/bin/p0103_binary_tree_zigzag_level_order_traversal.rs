use std::rc::Rc;
use std::cell::RefCell;

fn main() {}

// Definition for a binary tree node.
#[derive(Debug, PartialEq, Eq)]
pub struct TreeNode {
    pub val: i32,
    pub left: Option<Rc<RefCell<TreeNode>>>,
    pub right: Option<Rc<RefCell<TreeNode>>>,
}

impl TreeNode {
    #[inline]
    pub fn new(val: i32) -> Self {
        TreeNode {
            val,
            left: None,
            right: None
        }
    }
}

struct Solution;

impl Solution {
    pub fn zigzag_level_order(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<Vec<i32>> {

        if root.is_none() { return vec![]; }

        let root = root.unwrap();
        let mut res = vec![];
        let mut forward_stack = vec![];
        let mut backward_stack = vec![];

        forward_stack.push(Rc::clone(&root));

        while !forward_stack.is_empty() || !backward_stack.is_empty() {
            let mut level = vec![];
            while !forward_stack.is_empty() {
                let node = forward_stack.pop().unwrap();

                level.push(node.borrow().val);

                if let Some(ref left) = node.borrow().left {
                    backward_stack.push(Rc::clone(left));
                };
                if let Some(ref right) = node.borrow().right {
                    backward_stack.push(Rc::clone(right));
                };
            }
            if !level.is_empty() { res.push(level); }

            let mut level = vec![];
            while !backward_stack.is_empty() {
                let node = backward_stack.pop().unwrap();

                level.push(node.borrow().val);

                if let Some(ref right) = node.borrow().right {
                    forward_stack.push(Rc::clone(right));
                };
                if let Some(ref left) = node.borrow().left {
                    forward_stack.push(Rc::clone(left));
                };
            }
            if !level.is_empty() { res.push(level); }
        }

        res
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let root = TreeNode::new(3);

        assert_eq!(
            Solution::zigzag_level_order(Some(Rc::new(RefCell::new(root)))),
            vec![vec![3]]
        );
    }

    #[test]
    fn test2() {
        let mut root = TreeNode::new(3);
        root.left = Some(Rc::new(RefCell::new(TreeNode::new(4))));
        root.right = Some(Rc::new(RefCell::new(TreeNode::new(5))));

        assert_eq!(
            Solution::zigzag_level_order(Some(Rc::new(RefCell::new(root)))),
            vec![vec![3], vec![5, 4]]
        );
    }

    #[test]
    fn test3() {
        let mut root = TreeNode::new(3);
        let mut node = TreeNode::new(9);
        node.left = Some(Rc::new(RefCell::new(TreeNode::new(8))));
        node.right = Some(Rc::new(RefCell::new(TreeNode::new(6))));

        root.left = Some(Rc::new(RefCell::new(TreeNode::new(20))));
        root.right = Some(Rc::new(RefCell::new(node)));

        assert_eq!(
            Solution::zigzag_level_order(Some(Rc::new(RefCell::new(root)))),
            vec![vec![3], vec![9, 20], vec![8, 6]]
        );
    }
}