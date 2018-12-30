
fn main() {}

// Definition for singly-linked list.
#[derive(PartialEq, Eq, Debug)]
pub struct ListNode {
  pub val: i32,
  pub next: Option<Box<ListNode>>
}

impl ListNode {
  #[inline]
  fn new(val: i32) -> Self {
    ListNode {
      next: None,
      val
    }
  }
}

struct Solution;

impl Solution {
    pub fn reverse_list(head: Option<Box<ListNode>>) -> Option<Box<ListNode>> {
        if head.is_none() {
            return None;
        }
        let mut head = head;
        let mut new_head = head.take().unwrap();
        let mut next_node = new_head.next.take();

        while let Some(mut curr_node) = next_node.take() {
            next_node = curr_node.next.take();
            curr_node.next = Some(new_head);
            new_head = curr_node;
        }

        Some(new_head)
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let list = None;
        assert_eq!(Solution::reverse_list(list), None);
    }

    #[test]
    fn test2() {
        let list = Some(Box::new(ListNode {
            val: 1,
            next: None,
        }));

        let expected = Some(Box::new(ListNode {
            val: 1,
            next: None,
        }));
        assert_eq!(Solution::reverse_list(list), expected);
    }

    #[test]
    fn test3() {
        let list = Some(Box::new(ListNode {
            val: 1,
            next: Some(Box::new(ListNode {
                val: 2,
                next: Some(Box::new(ListNode {
                    val: 3,
                    next: Some(Box::new(ListNode {
                        val: 4,
                        next: None,
                    })),
                })),
            })),
        }));

        let expected = Some(Box::new(ListNode {
            val: 4,
            next: Some(Box::new(ListNode {
                val: 3,
                next: Some(Box::new(ListNode {
                    val: 2,
                    next: Some(Box::new(ListNode {
                        val: 1,
                        next: None,
                    })),
                })),
            })),
        }));
        assert_eq!(Solution::reverse_list(list), expected);
    }
}