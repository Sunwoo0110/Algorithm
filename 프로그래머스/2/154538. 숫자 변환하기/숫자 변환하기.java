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
        
        // BFS
//         Queue<Integer> queue = new ArrayDeque<>();
//         queue.add(x);

//         while (!queue.isEmpty()) {
//             int cur = queue.poll();
//             // 이미 y에 도달한 경우 더 이상 진행X
//             if (cur == y) return dp[cur];
//             for (int next : new int[]{cur+n, cur*2, cur*3}) {
//                 if (next > y) continue;
//                 if (dp[next] == -1 || dp[next] > dp[cur] + 1) {
//                     dp[next] = dp[cur]+1;
//                     queue.add(next);
//                 }
//             }
//         }
//         return -1;
        
        return dp[y];
    }
}