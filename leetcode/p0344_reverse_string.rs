
fn main() {}

struct Solution;

impl Solution {
    pub fn reverse_string(s: String) -> String {
        let mut s = s;

        unsafe {
            s.as_mut_vec().reverse();
        }

        s
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let s = Solution::reverse_string("hello".to_string());
        assert_eq!(s.as_str(), "olleh");
    }

    #[test]
    fn test2() {
        let s = Solution::reverse_string("A man, a plan, a canal: Panama".to_string());
        assert_eq!(s.as_str(), "amanaP :lanac a ,nalp a ,nam A");
    }
}
