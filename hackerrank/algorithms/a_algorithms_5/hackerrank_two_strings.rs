use std::io;
use std::collections::HashSet;
use std::fs::File;
use std::env;
use std::io::prelude::*;

fn two_strings(s1: &str, s2: &str) -> bool {
    let set1: HashSet<u8> = s1.bytes().collect();
    let set2: HashSet<u8> = s2.bytes().collect();

    let res: HashSet<_> = set1.intersection(&set2).collect();

    res.is_empty()
}

fn main() {

    let mut f = File::create(env::var("OUTPUT_PATH").unwrap()).unwrap();
//    let mut f = File::create("RESULT.txt").unwrap();

    let mut tests = String::new();
    let mut s1: String = String::new();
    let mut s2: String = String::new();

    io::stdin().read_line(&mut tests).unwrap();

    let n: u32 = tests.trim().parse().unwrap();

    for i in 0..n {
        s1.clear();
        s2.clear();

        io::stdin().read_line(&mut s1).unwrap();
        io::stdin().read_line(&mut s2).unwrap();

        let empty = two_strings(s1.trim(), s2.trim());

        if empty {
            f.write(b"NO\n");
        } else {
            f.write(b"YES\n");
        }
    }
}