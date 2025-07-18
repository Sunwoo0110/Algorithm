import java.util.*;

class Solution {
    public int solution(int m, int n, String[] board) {
        int answer = 0;
        
        char[][] map = new char[m][n];
        
        // CharArray로 변경
        for (int i=0; i<m; i++) {
            map[i] = board[i].toCharArray();
        }

        boolean changed = true;
        
        while (changed) {
            changed = false;
            
            boolean[][] remove = new boolean[m][n];

            // 2x2 같은 블록 찾기
            for (int i=0; i<m-1; i++) {
                for (int j=0; j<n-1; j++) {
                    char c = map[i][j];
                    
                    if (c != ' ' && c == map[i][j+1] && c == map[i+1][j] && c == map[i+1][j+1]) {
                        // 블록 삭제 저장
                        remove[i][j] = remove[i][j+1] = remove[i+1][j] = remove[i+1][j+1] = true;
                        changed = true;
                    }
                }
            }
            
            // 블록 삭제하고, 카운트
            for (int i=0; i<m; i++) {
                for (int j=0; j<n; j++) {
                    if (remove[i][j]) {
                        map[i][j] = ' ';
                        answer++;
                    }
                }
            }
            
            // 아래로 내리기
            for (int j=0; j<n; j++) {
                int k = m-1; // 맨 아래줄부터 시작
                for (int i=m-1; i>=0; i--) {
                    if (map[i][j] != ' ') {
                        // 블록 아래부터 채우기
                        map[k][j] = map[i][j];
                        --k;
                    }
                }
                // 위에 남은 빈칸 채우기
                for (int i=0; i<=k; i++){
                    map[i][j] = ' ';
                }
            }
        }
        return answer;
    }
}
