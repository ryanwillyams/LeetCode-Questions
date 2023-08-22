class Solution {
public:
    int longestConsecutive(vector<int>& nums) {
        if(nums.size() == 0) return 0;
        std::priority_queue c3(std::less<int>(), nums);
        int con=1;
        int maxCon =con;
        int top;
        
        for(int x =c3.size()-1; x >= 0; x--){
            int toptop = c3.top();
            c3.pop();
            top = c3.top();
             if(top == toptop){
                 
                 continue;
             }
            
            if(c3.top() == toptop-1){
                con++;
            if(maxCon < con)
            maxCon = con;

            }
            else{
                con =1;
            }
           
            }
       return maxCon;


        
    }
};