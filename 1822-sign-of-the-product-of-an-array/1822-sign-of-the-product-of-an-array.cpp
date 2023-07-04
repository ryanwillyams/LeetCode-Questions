class Solution {
public:
    int arraySign(vector<int>& nums) {
        int ans;
        if(nums.size() == 1){
            if(nums[0]  >= 1){
            ans =1;
        }
             
           else if(nums[0]  <= -1)
            ans =-1;
            
        else
    
            ans = 0;
            
        
            return ans;
        }
        int value = signFunc(nums);
       
        
        
        
        return value;
    }
    
    int signFunc(vector<int> &vect){
        int n = vect[0];
        for(int x =1; x < vect.size(); x++){
           if((n * vect[x]) > 0){
               n = 1;
           }
            else if((n * vect[x]) < 0){
                n = -1;
            }
            
            else {
                n = 0;
            }
            
            
            
        }
        return n;
    }
};