import java.util.*;

class Solution {
    int solution(int[][] land) {
        int answer = 0;
        int len = land.length;
        
        for(int i=1; i<len; ++i){
            for (int j=0; j<4; ++j) {
                int max = 0;
                for (int k=0; k<4; ++k) {
                    if (j == k) continue; // 같은 열은 못 밟음
                    max = Math.max(max, land[i-1][k]);
                }
                land[i][j] += max;
            }
        }
        
        for (int val : land[len-1]) {
            answer = Math.max(answer, val);
        }
        return answer;
    }
}