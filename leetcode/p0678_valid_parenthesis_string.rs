
fn main() {}

struct Solution;

impl Solution {

    fn search(stack: Vec<char>, current_s: &[char]) -> bool {
        if current_s.len() < stack.len() { // tree pruning
            return false;
        }
        if current_s.is_empty() {
            if stack.is_empty() { return true; }
            else { return false; }
        }

        // tree pruning
        let mut star_cnt = 0;
        let mut left_cnt = stack.len();
        let mut right_cnt = 0;
        for &i in current_s {
            match i {
                '(' => left_cnt += 1,
                ')' => right_cnt +=1,
                _ => star_cnt +=1,
            }
        }
        if left_cnt > star_cnt + right_cnt {
            return false;
        }

        let c = current_s[0];
        if c == '*' {
            let mut new_stack1 = stack.clone();
            let new_stack2 = stack.clone();
            let mut new_stack3 = stack.clone();
            new_stack1.push('(');
            new_stack3.pop();
            let res1 = Solution::search(new_stack1, &current_s[1..]);
            if res1 == true {
                return res1;
            }
            let res2 = Solution::search(new_stack2, &current_s[1..]);
            if res2 == true {
                return res2;
            }
            let res3 = Solution::search(new_stack3, &current_s[1..]);
            if res3 == true {
                return res3;
            }
            return false;
        }
        if c == '(' {
            let mut new_stack = stack.clone();
            new_stack.push('(');
            return Solution::search(new_stack, &current_s[1..]);
        }
        if c == ')' {
            if stack.is_empty() {
                return false;
            }
            let mut new_stack = stack.clone();
            new_stack.pop();
            return Solution::search(new_stack, &current_s[1..]);
        }
        false
    }

    // TODO: find another solution
    pub fn check_valid_string(s: String) -> bool {
        let chars: Vec<char> = s.chars().collect();
        Solution::search(vec![], &chars)
    }
}

#[cfg(test)]
mod tests {

    use super::*;

    #[test]
    fn test1() {
        assert_eq!(Solution::check_valid_string("()".to_string()), true);
        assert_eq!(Solution::check_valid_string("(*)".to_string()), true);
        assert_eq!(Solution::check_valid_string("(*))".to_string()), true);
        assert_eq!(Solution::check_valid_string("**)".to_string()), true);
        assert_eq!(Solution::check_valid_string("(**".to_string()), true);
        assert_eq!(Solution::check_valid_string("(".to_string()), false);
        assert_eq!(Solution::check_valid_string(")".to_string()), false);
        assert_eq!(Solution::check_valid_string(")*".to_string()), false);
        assert_eq!(Solution::check_valid_string("(*".to_string()), true);
        assert_eq!(Solution::check_valid_string("())".to_string()), false);
        assert_eq!(Solution::check_valid_string("(()".to_string()), false);
        assert_eq!(Solution::check_valid_string("((****)".to_string()), true);
        assert_eq!(Solution::check_valid_string("(****))".to_string()), true);
    }

    #[test]
    fn test2() {
        let s = "(((((*(()((((*((**(((()()*)()()()*((((**)())*)*)))))))(())(()))())((*()()(((()((()*(())*(()**)()(())";
        assert_eq!(Solution::check_valid_string(s.to_string()), false);
    }

    #[test]
    fn test3() {
        let s = "(((((*(((((*((**(((*)*((((**))*)*)))))))))((*(((((**(**)";
        assert_eq!(Solution::check_valid_string(s.to_string()), false);
    }
}
