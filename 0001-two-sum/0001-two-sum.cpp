class Solution {
public:
    vector<int> twoSum(vector<int>& nums, int target){
        vector<int> answer;
        for(int x =0; x < nums.size(); x++){
            for(int y = nums.size()-1; y > x; y--){
                if(nums[y] == target - nums[x]){
                    
                    answer.push_back(y);
                    answer.push_back(x);
                }
            }
        }
    return answer;
    }
};