/**
 * @param {string} s
 * @return {number}
 */
//do two loops one for the whole string and 1 for each letter consecutive length
var lengthOfLongestSubstring = function(s) {
    let str = new Set();
    
    let max=0;
    
    
    for(let i = 0; i < s.length; i++){
        str.clear();
        for(let j = i; j < s.length; j++ ){
            if(str.has(s[j])){
                max = max > str.size ? max : str.size;
                j = s.length;
            }
            else{
                str.add(s[j]);
                max = (max > str.size) ? max : str.size;
            }
        }
    }

    
    
    return max;
};