class Solution:
    def maximumTime(self, time: str) -> str:
        
        ans =""
        if(time[4].isdigit()):
            ans += time[4]
        else:
           ans += "9"
        if(time[3].isdigit()):
            ans += time[3]
            ans += ":"
        else:
            ans += "5"
            ans += ":"
        if(time[1].isdigit()):
            ans += time[1]
        elif(time[0].isdigit() and time[0] != "2"):
            ans += "9"
        else:
            ans += "3"
        if(time[0].isdigit()):
            ans += time[0]
        elif(int(ans[3]) > 3):
            ans+= "1"
        else:
            ans += "2"
        reversedAns = ''.join(reversed(ans))
        return reversedAns
         



