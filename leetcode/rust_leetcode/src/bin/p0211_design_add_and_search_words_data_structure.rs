use std::collections::HashMap;

fn main() {}

struct Node {
    is_ending: bool,
    children: HashMap<char, Node>,
}

impl Node {
    fn new() -> Self {
        Node {
            is_ending: false,
            children: HashMap::new(),
        }
    }
}

struct WordDictionary {
    root: Node,
}

/**
  * `&self` means the method takes an immutable reference
  * If you need a mutable reference, change it to `&mut self` instead.
 */
impl WordDictionary {

    fn new() -> Self {
        WordDictionary {
            root: Node::new(),
        }
    }

    fn add_word(&mut self, word: String) {
        self.add_to_trie(word);
    }

    // for example, "abc.de", the prefix "abc" has been searched
    // but after replacing and generating new word, we search from scratch again which is slow
    fn TLE_search(&self, word: String) -> bool {
        if !word.contains(".") {
            self.trie_contains(word)
        } else {
            ('a'..='z').any(|c| {
                let new_word = word.replacen(".", c.to_string().as_str(), 1);
                self.search(new_word)
            })
        }
    }

    // refer to https://leetcode.com/problems/design-add-and-search-words-data-structure/solutions/1725327/java-c-python-a-very-well-detailed-explanation/
    fn search(&self, word: String) -> bool {
        fn _search(root: &Node, w: &str) -> bool {
            let mut curr = Some(root);
            for (i, v) in w.chars().enumerate() {
                if curr.is_none() { break }
                if v == '.' {
                    return curr.unwrap().children.values().any(|node| {
                        _search(node, &w[i+1..])
                    })
                }
                curr = curr.unwrap().children.get(&v)
            }
            curr.is_some() && curr.unwrap().is_ending
        }

        _search(&self.root, word.as_str())
    }

    fn add_to_trie(&mut self, s: String) {
        let mut curr = &mut self.root;
        for c in s.chars() {
            curr = curr.children.entry(c).or_insert(Node::new());
        }
        curr.is_ending = true;
    }

    fn trie_contains(&self, s: String) -> bool {
        let mut curr = Some(&self.root);
        for c in s.chars() {
            if curr.is_none() { break }
            curr = curr.unwrap().children.get(&c)
        }
        match curr {
            None => false,
            Some(node) => node.is_ending,
        }
    }
}

/**
 * Your WordDictionary object will be instantiated and called as such:
 * let obj = WordDictionary::new();
 * obj.add_word(word);
 * let ret_2: bool = obj.search(word);
 */
#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test() {
        let mut word_dict = WordDictionary::new();
        word_dict.add_word("bad".to_string());
        word_dict.add_word("dad".to_string());
        word_dict.add_word("mad".to_string());
        assert_eq!(word_dict.search("pad".to_string()), false);
        assert_eq!(word_dict.search("bad".to_string()), true);
        assert_eq!(word_dict.search(".ad".to_string()), true);
        assert_eq!(word_dict.search("b..".to_string()), true);
    }
}
