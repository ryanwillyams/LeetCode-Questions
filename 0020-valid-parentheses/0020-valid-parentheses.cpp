class Solution {
public:
    bool isValid(string s) {
        if(s.length() == 0 || s.length() == 1) return false;
        map<char,char> m;
        stack<char> stack;
        m.insert({']','['});
        m.insert({'}','{'});
        m.insert({')','('});

        for(int x= 0; x < s.length(); x++){
            if(m.contains(s[x]) && stack.size() > 0){
                if(m[s[x]] == stack.top()){
                    stack.pop();
                continue;
                }
                else return false;
            }

            stack.push(s[x]);
            
        }
        
            return (stack.size() == 0);

    }
};