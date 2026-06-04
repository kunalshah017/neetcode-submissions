impl Solution {
    pub fn is_anagram(s: String, t: String) -> bool {
        if s.len() != t.len(){
            return false
        }

        let mut s_vec: Vec<char> = s.chars().collect();
        s_vec.sort_unstable();
        
        let mut t_vec: Vec<char> = t.chars().collect();
        t_vec.sort_unstable();

        for i in 0..s_vec.len(){
            if s_vec[i] != t_vec[i]{
                return false;
            }
        }

        return true;
    }
}
