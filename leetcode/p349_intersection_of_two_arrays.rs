use std::collections::HashSet;

fn main() {}

struct Solution;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let set1: HashSet<_> = nums1.iter().cloned().collect();
        let set2: HashSet<_> = nums2.iter().cloned().collect();

        let set: Vec<_> = set1.intersection(&set2).cloned().collect();

        set
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let nums1 = [1,2,2,1];
        let nums2 = [2,2];

        let mut res = Solution::intersection(nums1.to_vec(), nums2.to_vec());

        res.sort();
        assert_eq!(res, vec![2]);
    }

    #[test]
    fn test2() {
        let nums1 = [4, 9, 5];
        let nums2 = [9, 4, 9, 8, 4];

        let mut res = Solution::intersection(nums1.to_vec(), nums2.to_vec());

        res.sort();
        assert_eq!(res, vec![4, 9]);
    }
}
