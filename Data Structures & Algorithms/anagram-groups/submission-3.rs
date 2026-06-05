impl Solution {
    pub fn group_anagrams(strs: Vec<String>) -> Vec<Vec<String>> {
        let mut hashmap: HashMap<Vec<char>, Vec<String>> = HashMap::new();

        for string in strs{
            let mut string_vec: Vec<char> = string.chars().collect();
            string_vec.sort_unstable();

            hashmap
                .entry(string_vec)
                .or_insert(Vec::new())
                .push(string)
        }
        
        return hashmap.into_values().collect();
    }
}
