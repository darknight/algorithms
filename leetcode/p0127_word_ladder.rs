
fn main() {}

struct Solution;

impl Solution {
    pub fn ladder_length(begin_word: String, end_word: String, word_list: Vec<String>) -> i32 {
        use std::collections::{HashMap, HashSet};
        use std::time::SystemTime;

        if !word_list.contains(&end_word) {
            return 0;
        }
        for word in word_list.iter() {
            if Solution::connected(begin_word.as_str(), word.as_str()) {
                break
            }
        }

        let mut word_list = word_list;
        word_list.push(begin_word.clone());

        let x = SystemTime::now();
        let mut graph = vec![vec![];word_list.len()];
        for i in 0..word_list.len() - 1{
            for j in i + 1..word_list.len() {
                if Solution::connected(word_list[i].as_str(), word_list[j].as_str()) {
                    graph[i].push(j);
                    graph[j].push(i);
                }
            }
        }

        let mut res = 0;
        let target = word_list.iter().position(|x| x == &end_word).unwrap();
        let mut visited = vec![false; word_list.len()];
        let mut queue = vec![word_list.len() - 1];
        while !queue.is_empty() {
            res += 1;
            for &index in queue.iter() {
                if index == target {
                    return res;
                }
                visited[index] = true;
            }
            let indices: Vec<_> = queue.drain(..).collect();
            for index in indices {
                for &next_index in graph[index].iter() {
                    if !visited[next_index] {
                        visited[next_index] = true;
                        queue.push(next_index);
                    }
                }
            }
        }
        return 0;
    }

    fn connected(word1: &str, word2: &str) -> bool {
        let mut cnt = 0;
//        let chars1: Vec<_> = word1.chars().collect(); // very slow
        let bytes1 = word1.as_bytes();
        let bytes2 = word2.as_bytes();
        for i in 0..bytes1.len() {
            if cnt > 1 {
                return false
            }
            if bytes1[i] != bytes2[i] {
                cnt += 1;
            }
        }
        cnt == 1
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        let v1 = vec!["hot","dot","dog","lot","log","cog"].iter().map(|&w| w.to_string()).collect();
        assert_eq!(Solution::ladder_length("hit".to_string(), "cog".to_string(), v1), 5);

        let v2 = vec!["hot","dot","dog","lot","log"].iter().map(|&w| w.to_string()).collect();
        assert_eq!(Solution::ladder_length("hit".to_string(), "cog".to_string(), v2), 0);

        let v3 = vec!["lest","leet","lose","code","lode","robe","lost"].iter().map(|&w| w.to_string()).collect();
        assert_eq!(Solution::ladder_length("leet".to_string(), "code".to_string(), v3), 6);
    }
}