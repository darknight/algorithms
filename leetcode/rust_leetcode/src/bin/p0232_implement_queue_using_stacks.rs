
fn main() {}

struct MyQueue{
    push_stack: Vec<i32>,
    pop_stack: Vec<i32>,
}

/**
 * `&self` means the method takes an immutable reference.
 * If you need a mutable reference, change it to `&mut self` instead.
 */
impl MyQueue {

    /** Initialize your data structure here. */
    fn new() -> Self {
        MyQueue { push_stack: vec![], pop_stack: vec![] }
    }

    /** Push element x to the back of queue. */
    fn push(&mut self, x: i32) {
        self.push_stack.push(x)
    }

    /** Removes the element from in front of queue and returns that element. */
    fn pop(&mut self) -> i32 {
        if self.pop_stack.is_empty() {
            let data = self.push_stack.drain(..);
            self.pop_stack.extend(data.rev());
        }
        self.pop_stack.pop().unwrap()
    }

    /** Get the front element. */
    fn peek(&mut self) -> i32 {
        if self.pop_stack.is_empty() {
            let data = self.push_stack.drain(..);
            self.pop_stack.extend(data.rev());
        }
        *self.pop_stack.last().unwrap()
    }

    /** Returns whether the queue is empty. */
    fn empty(&self) -> bool {
        self.pop_stack.is_empty() && self.push_stack.is_empty()
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let mut q = MyQueue::new();
        q.push(1);
        q.push(2);
        assert_eq!(q.peek(), 1);
        assert_eq!(q.pop(), 1);
        assert_eq!(q.empty(), false);
    }

    #[test]
    fn test2() {
        let mut q = MyQueue::new();
        q.push(1);
        q.push(2);
        q.push(3);
        assert_eq!(q.pop(), 1);
        q.push(4);
        assert_eq!(q.pop(), 2);
        assert_eq!(q.pop(), 3);
        assert_eq!(q.pop(), 4);
        assert_eq!(q.empty(), true);
    }
}