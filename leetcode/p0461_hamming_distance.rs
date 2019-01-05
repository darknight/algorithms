
fn main() {}

struct Solution;

impl Solution {
    pub fn hamming_distance(x: i32, y: i32) -> i32 {
        let mut res = 0;
        let mut xor = x ^ y;

        while xor != 0 {
            res += xor % 2;
            xor = xor >> 1;
        }

        res
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::hamming_distance(1, 4), 2);
    }

    #[test]
    fn test2() {
    }
}