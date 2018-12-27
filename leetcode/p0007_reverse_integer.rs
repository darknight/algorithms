
fn main() {}

struct Solution;

impl Solution {
    pub fn reverse(x: i32) -> i32 {
        if x == i32::min_value() {
            return 0;
        }
        let negative = if x < 0 { true } else { false };
        let mut x = x.abs();

        let mut res: i32 = 0;
        while x != 0 {
            let remainder = x % 10;
            x = x / 10;
            // test if overflow
            if res.wrapping_mul(10i32) / 10 != res {
                return 0;
            }
            res = res * 10 + remainder;
        }

        if negative {
            -res
        } else {
            res
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::reverse(123), 321);
        assert_eq!(Solution::reverse(-123), -321);
        assert_eq!(Solution::reverse(120), 21);
        assert_eq!(Solution::reverse(-2147483648), 0);
        assert_eq!(Solution::reverse(1534236469), 0);
    }
}