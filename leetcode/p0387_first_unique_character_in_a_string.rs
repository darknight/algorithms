use std::collections::HashMap;

fn main() {}

struct Solution;

impl Solution {
    pub fn first_uniq_char(s: String) -> i32 {
        let mut map = HashMap::new();
        let chars: Vec<char> = s.chars().collect();
        for c in chars.iter() {
            let counter = map.entry(c).or_insert(0);
            *counter += 1;
        }
        for i in 0..chars.len() {
            let c = chars[i];
            if *map.get(&c).unwrap() == 1 {
                return i as i32;
            }
        }

        -1
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::first_uniq_char(String::from("leetcode")), 0);
        assert_eq!(Solution::first_uniq_char(String::from("loveleetcode")), 2);
        assert_eq!(Solution::first_uniq_char(String::from("helloolleh")), -1);
    }
}