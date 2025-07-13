import java.util.*;

class Solution {
    public int solution(int sticker[]) {
        int n = sticker.length;
        if (n == 1) return sticker[0];
        if (n == 2) return Math.max(sticker[0], sticker[1]);
        
        // 1. 맨 앞을 뜯는 경우 (마지막 못 뜯음)
        int[] dp1 = new int[n];
        dp1[0] = sticker[0];
        dp1[1] = Math.max(sticker[0], sticker[1]);
        
        for (int i=2; i<n-1; i++) {
            dp1[i] = Math.max(dp1[i-1], dp1[i-2]+sticker[i]);
        }

        // 2. 맨 앞을 안 뜯는 경우 (1~n-1만 가능)
        int[] dp2 = new int[n];
        dp2[0] = 0;
        dp2[1] = sticker[1];
        for (int i=2; i<n; i++) {
            dp2[i] = Math.max(dp2[i-1], dp2[i-2]+sticker[i]);
        }

        return Math.max(dp1[n-2], dp2[n-1]);
    }
}