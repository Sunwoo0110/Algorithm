import java.util.*;

class Solution {
    int answer = 0;
    
    public int solution(int n) {
        int[] queens = new int[n]; // queens[row] = row에 있는 column 번호
        placeQueen(n, 0, queens);
        return answer;
    }
    
    public void placeQueen(int n, int row, int[] queens){
        if(row == n) {
            answer++;
            return ;
        }
        
        for(int col=0; col<n; col++){
            if (isSafe(row, col, queens)) {
                queens[row] = col;
                placeQueen(n, row+1, queens);
            }
        }
    }
    
    public boolean isSafe(int row, int col, int[] queens){
        // 해당 위치가 가능한 지 확인
        for (int i = 0; i < row; i++) {
            if (queens[i] == col) return false; // 같은 열
            if (Math.abs(row - i) == Math.abs(col - queens[i])) return false; // 대각선
        }
        return true;
    }
}