impl Solution {
    pub fn has_duplicate(nums: Vec<i32>) -> bool {
        let nums_set: HashSet<_> = nums.iter().copied().collect();
        if nums_set.len() == nums.len(){
            return false
        } 
        else {
            return true
        }
    }
}
