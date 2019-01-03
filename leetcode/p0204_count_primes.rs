
fn main() {}

struct Solution;

impl Solution {
    pub fn count_primes(n: i32) -> i32 {
        let n = n - 1;
        match n {
            i if i <= 1 => 0,
            2 => 1, //[2]
            3 => 2, //[2,3]
            _ => {
                let mut res = vec![2, 3];
                res.extend((4..n + 1).filter(|&val| Self::is_prime(val)));
                res.len() as i32
            }
        }
    }

    fn is_prime(target: i32) -> bool {
        let upper = (target as f64).sqrt() as i32;
        for i in 2..upper + 1 {
            if target % i == 0 {
                return false;
            }
        }
        true
    }

    ///
    /// far slower than submitted version
    ///
    pub fn count_primes2(n: i32) -> i32 {
        let n = n - 1;
        match n {
            i if i <= 1 => 0,
            2 => 1, //[2]
            3 => 2, //[2,3]
            _ => {
                let mut res = vec![2, 3];
                let upper = ((n + 1) as f64).sqrt() as i32;
                for val in 4..upper {
                    if res.iter().find(|&&x| val % x == 0).is_none() {
                        res.push(val);
                    }
                }
                res.len() as i32
            }
        }
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::count_primes(1), 0);
        assert_eq!(Solution::count_primes(2), 0);
        assert_eq!(Solution::count_primes(3), 1);
        assert_eq!(Solution::count_primes(11), 4);
        assert_eq!(Solution::count_primes(1001), 168);
        assert_eq!(Solution::count_primes(10001), 1229);
        assert_eq!(Solution::count_primes(100001), 9592);
        assert_eq!(Solution::count_primes(1000001), 78498);
    }
}