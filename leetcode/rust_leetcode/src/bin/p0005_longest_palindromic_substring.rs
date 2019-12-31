
fn main() {}

struct Solution;

impl Solution {
    pub fn longest_palindrome(s: String) -> String {
        if s.len() == 0 { return String::new(); }
        if s.len() == 1 { return s.to_string(); }

        let s: Vec<char> = s.chars().collect();
        let mut upper_bound = s.len();
        while upper_bound > 0 {
            for i in 0..s.len() - upper_bound + 1 {
                let candidate = &s[i..i + upper_bound];
                if Self::is_palindrom(candidate) {
                    let res: String = candidate.iter().collect();
                    return res;
                }
            }
            upper_bound -= 1;
        }

        unreachable!()
    }

    fn is_palindrom(s: &[char]) -> bool {
        let mut i = 0;
        let mut j = s.len() - 1;
        loop {
            if s[i] != s[j] {
                return false;
            }
            if j == 0 { break; }
            i += 1;
            j -= 1;
        }
        return true;
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::longest_palindrome("ac".to_string()), "a");
        assert_eq!(Solution::longest_palindrome("aa".to_string()), "aa");
        assert_eq!(Solution::longest_palindrome("babad".to_string()), "bab");
        assert_eq!(Solution::longest_palindrome("cbbd".to_string()), "bb");
    }
}