impl Solution {
    pub fn two_sum(nums: Vec<i32>, target: i32) -> Vec<i32> {
        let mut hashmap = HashMap::new();

        for (index, num) in nums.iter().enumerate() {
            if hashmap.contains_key(&(target - num)){
                let result: Vec<i32> = vec![hashmap[&(target - num)], index as i32];
                return result
            }else{
                hashmap.insert(num, index as i32);
            }
        }

        return vec![]
    }
}
