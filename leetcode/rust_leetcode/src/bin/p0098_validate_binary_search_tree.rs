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

    fn traverse_bst(root: Option<Rc<RefCell<TreeNode>>>) -> Vec<i32> {
        if let Some(node) = root {
            let left = if node.borrow().left.is_some() {
                Some(Rc::clone(node.borrow().left.as_ref().unwrap()))
            } else {
                None
            };
            let mut res = Self::traverse_bst(left);

            res.push(node.borrow().val);

            let right = if node.borrow().right.is_some() {
                Some(Rc::clone(node.borrow().right.as_ref().unwrap()))
            } else {
                None
            };
            let mut res2 = Self::traverse_bst(right);
            res.append(&mut res2);

            res
        } else {
            Vec::new()
        }
    }

    pub fn is_valid_bst(root: Option<Rc<RefCell<TreeNode>>>) -> bool {
        let res = Self::traverse_bst(root);
        if res.len() <= 1 { return true; }
        for i in 0..res.len() - 1 {
            if res[i] >= res[i + 1] {
                return false
            }
        }

        true
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test0() {
        let root = None;

        assert_eq!(Solution::is_valid_bst(root), true);
    }

    #[test]
    fn test1() {
        let mut root = TreeNode::new(2);
        root.left = Some(Rc::new(RefCell::new(TreeNode::new(1))));
        root.right = Some(Rc::new(RefCell::new(TreeNode::new(3))));

        assert_eq!(Solution::is_valid_bst(Some(Rc::new(RefCell::new(root)))), true);
    }

    #[test]
    fn test2() {
        let mut root = TreeNode::new(5);
        let mut node = TreeNode::new(4);
        node.left = Some(Rc::new(RefCell::new(TreeNode::new(3))));
        node.right = Some(Rc::new(RefCell::new(TreeNode::new(6))));

        root.left = Some(Rc::new(RefCell::new(TreeNode::new(1))));
        root.right = Some(Rc::new(RefCell::new(node)));

        assert_eq!(Solution::is_valid_bst(Some(Rc::new(RefCell::new(root)))), false);
    }

    #[test]
    fn test3() {
        let mut root = TreeNode::new(1);
        root.left = Some(Rc::new(RefCell::new(TreeNode::new(1))));

        assert_eq!(Solution::is_valid_bst(Some(Rc::new(RefCell::new(root)))), false);
    }
}