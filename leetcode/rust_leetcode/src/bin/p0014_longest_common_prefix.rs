
fn main() {}

struct Solution;

impl Solution {
    pub fn longest_common_prefix(strs: Vec<String>) -> String {
        if strs.len() < 1 {
            return "".to_string();
        }
        if strs.len() == 1 {
            let mut strs = strs;
            return strs.pop().unwrap();
        }

        let chars: Vec<Vec<char>> = strs.iter().map(|s| s.chars().collect()).collect();
        let mut res = String::new();

        let mut j = 0;
        loop {
            if j >= chars[0].len() { break; }

            let curr_char = chars[0][j];

            let mut i = 1;
            while i < chars.len() {
                if j >= chars[i].len() { break; }
                else if chars[i][j] != curr_char { break; }
                else { i += 1; }
            }

            if i < chars.len() { break; }
            else {
                res.push(curr_char);
                j += 1;
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
        let input = vec!["flower","flow","flight"];
        let res = Solution::longest_common_prefix(
            input.into_iter().map(|s| s.to_string()).collect()
        );
        assert_eq!(res, "fl");
    }

    #[test]
    fn test2() {
        let input = vec!["dog","racecar","car"];
        let res = Solution::longest_common_prefix(
            input.into_iter().map(|s| s.to_string()).collect()
        );
        assert_eq!(res, "");
    }

    #[test]
    fn test3() {
        let input = vec!["","racecar"];
        let res = Solution::longest_common_prefix(
            input.into_iter().map(|s| s.to_string()).collect()
        );
        assert_eq!(res, "");
    }

    #[test]
    fn test4() {
        let input = vec!["r","racecar"];
        let res = Solution::longest_common_prefix(
            input.into_iter().map(|s| s.to_string()).collect()
        );
        assert_eq!(res, "r");
    }

    #[test]
    fn test5() {
        let input = vec!["a"];
        let res = Solution::longest_common_prefix(
            input.into_iter().map(|s| s.to_string()).collect()
        );
        assert_eq!(res, "a");
    }
}