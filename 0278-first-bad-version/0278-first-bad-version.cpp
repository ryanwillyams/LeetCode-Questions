class Solution {
public:
    int firstBadVersion(int n) {
        if(n == 1 ){
            return 1;
        }
        int counter = -1;
        
        int x = n/2;
        if(isBadVersion(x) == false){
            for(int y = x;x < n; x++){
            if(isBadVersion(y) == true){
                return y;
            }
        }
    }
        if(isBadVersion(x) == true){
            for(int z = x;z > 0; x--){
            if(isBadVersion(x) == false){

                return ++x;
            }
        }
    }
        
        if(counter == -1)
            
            return 1;
    
            return 0;
        }
    
        
    
};