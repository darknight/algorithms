use std::collections::HashSet;

fn main() {}

struct Solution;

impl Solution {
    pub fn intersection(nums1: Vec<i32>, nums2: Vec<i32>) -> Vec<i32> {
        let mut nums1 = nums1;
        let mut nums2 = nums2;
        let mut nums = Vec::new();
        nums1.sort();
        nums2.sort();

        let mut i = 0;
        let mut j = 0;

        while i < nums1.len() && j < nums2.len() {
            if nums1[i] > nums2[j] { j += 1; continue; }
            if nums1[i] == nums2[j] { nums.push(nums1[i]); i += 1; j += 1; continue; }
            if nums1[i] < nums2[j] { i += 1; continue; }
        }

        nums
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
        assert_eq!(res, vec![2, 2]);
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
