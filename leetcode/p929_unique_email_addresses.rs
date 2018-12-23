use std::collections::HashSet;

fn main() {}

struct Solution;

impl Solution {
    pub fn num_unique_emails(emails: Vec<String>) -> i32 {
        let mut sets = HashSet::new();

        for e in emails {
            let t: Vec<&str> = e.split('@').collect();
            let (local, domain) = (t[0], t[1]);

            let lt: Vec<&str> = local.split("+").collect();
            let local = lt[0];
            let local_string = local.replace(".", "");
            let email = format!("{}@{}", local_string, domain);

            sets.insert(email);
        }

        sets.len() as i32
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test() {

        let input = vec![
            "test.email+alex@leetcode.com".to_string(),
            "test.e.mail+bob.cathy@leetcode.com".to_string(),
            "testemail+david@lee.tcode.com".to_string()
        ];

        let res = Solution::num_unique_emails(input);

        assert_eq!(res, 2);
    }
}