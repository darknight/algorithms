
fn main() {}

struct Solution;

impl Solution {
    pub fn num_jewels_in_stones(j: String, s: String) -> i32 {
        let mut res = 0;
        for st in s.chars() {
            if j.find(st).is_some() {
                res += 1;
            }
        }

        res
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let j = "aA".to_string();
        let s = "aAAbbbb".to_string();

        assert_eq!(Solution::num_jewels_in_stones(j, s), 3);
    }

    #[test]
    fn test2() {
        let j = "z".to_string();
        let s = "ZZ".to_string();

        assert_eq!(Solution::num_jewels_in_stones(j, s), 0);
    }
}