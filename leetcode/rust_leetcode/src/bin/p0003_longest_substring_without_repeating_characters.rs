use std::collections::HashSet;

fn main() {}

struct Solution;

impl Solution {
    pub fn length_of_longest_substring(s: String) -> i32 {
        if s.len() == 0 { return 0; }
        if s.len() == 1 { return 1; }

        let chars: Vec<char> = s.chars().collect();
        let mut res = 0;
        let mut set = HashSet::new();
        let mut i = 0;
        let mut j = i;

        loop {
            if set.contains(&chars[j]) {
                res = res.max(j - i);
                while chars[i] != chars[j] {
                    set.remove(&chars[i]);
                    i += 1;
                }
                set.remove(&chars[i]);
                i += 1;
            } else {
                set.insert(chars[j]);
                j += 1;
                if j == chars.len() {
                    res = res.max(j - i);
                    break;
                }
            }
        }

        res as i32
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::length_of_longest_substring("aa".to_string()), 1);
        assert_eq!(Solution::length_of_longest_substring("ab".to_string()), 2);
        assert_eq!(Solution::length_of_longest_substring("aab".to_string()), 2);
        assert_eq!(Solution::length_of_longest_substring("abb".to_string()), 2);
        assert_eq!(Solution::length_of_longest_substring("aba".to_string()), 2);
        assert_eq!(Solution::length_of_longest_substring("abc".to_string()), 3);
    }
}