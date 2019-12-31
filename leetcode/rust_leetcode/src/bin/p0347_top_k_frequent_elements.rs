use std::collections::HashMap;
use std::collections::BinaryHeap;

fn main() {}

struct Solution;

impl Solution {
    pub fn top_k_frequent(nums: Vec<i32>, k: i32) -> Vec<i32> {
        if nums.len() <= 1 { return nums }

        let mut map = HashMap::new();
        for num in nums {
            let stat = map.entry(num).or_insert(1);
            *stat += 1;
        }

        let mut heap = BinaryHeap::new();
        for (k, v) in map {
            heap.push((v, k));
        }

        let mut sorted = heap.into_sorted_vec();
        sorted.reverse();

        sorted.iter().take(k as usize).map(|item| item.1).collect()
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::top_k_frequent(vec![1,1,1,2,2,3], 2), vec![1,2]);
        assert_eq!(Solution::top_k_frequent(vec![1,1,1,2,2,3], 3), vec![1,2,3]);
    }
}