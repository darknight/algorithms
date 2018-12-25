
fn main() {}

struct Solution;

impl Solution {
    pub fn fizz_buzz(n: i32) -> Vec<String> {

        let mut v = Vec::new();

        for i in 1..n+1 {
            if i % 15 == 0 { v.push("FizzBuzz".to_string()); }
            else if i % 3 == 0 { v.push("Fizz".to_string()); }
            else if i % 5 == 0 { v.push("Buzz".to_string()); }
            else { v.push(format!("{}", i)); }
        }

        v
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let res = Solution::fizz_buzz(15);
        let expected = vec![
            "1",
            "2",
            "Fizz",
            "4",
            "Buzz",
            "Fizz",
            "7",
            "8",
            "Fizz",
            "Buzz",
            "11",
            "Fizz",
            "13",
            "14",
            "FizzBuzz"
        ];

        assert_eq!(res, expected);
    }

}