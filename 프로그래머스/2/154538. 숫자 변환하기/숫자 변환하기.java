import java.util.*;

class Solution {
    public int solution(int x, int y, int n) {
        int answer = 0;
        
        int[] dp = new int[y+1];
        Arrays.fill(dp, -1);
        dp[x] = 0;
        
        while (x <= y){
            if(dp[x] == -1) {
                ++x;
                continue;
            }
            
            if(x+n <= y){
                dp[x+n] = dp[x+n] != -1 ? Math.min(dp[x]+1, dp[x+n]) : dp[x]+1;
            }
            if(x*2 <= y){
                dp[x*2] = dp[x*2] != -1 ? Math.min(dp[x]+1, dp[x*2]) : dp[x]+1;
            }
            if(x*3 <= y){
                dp[x*3] = dp[x*3] != -1 ? Math.min(dp[x]+1, dp[x*3]) : dp[x]+1;
            }
            x++;
        }
        
        return dp[y];
    }
}