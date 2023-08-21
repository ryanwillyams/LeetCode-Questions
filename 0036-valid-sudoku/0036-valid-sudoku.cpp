class Solution {
public:
    bool isValidSudoku(vector<vector<char>>& board) {
        set<char> row[9];
        set<char> col[9];
        set<char> box[9];
        for(int i=0;i<9;i++)
        {
            for(int j=0;j<9;j++)
            {
                
                if(board[i][j]=='.') continue;

                
                if(row[i].count(board[i][j])>=1) return false;
                else row[i].insert(board[i][j]);

                
                if(col[j].count(board[i][j])>=1) return false;
                else col[j].insert(board[i][j]);
                
                
               

                
                if(box[(i/3)*3 + (j/3)].count(board[i][j])>=1) return false;
                else box[(i/3)*3 + (j/3)].insert(board[i][j]);
            }
        }


        return true;
    }
};