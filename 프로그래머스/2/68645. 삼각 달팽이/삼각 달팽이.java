class Solution {
    public int[] solution(int n) {
        
        int len = n*(n+1)/2;
        int[] answer = new int[len];
        
        int[][] map = new int[n][n];
        
        // 순서: 아래 오른쪽 위
        int[] dx = {1, 0, -1};
        int[] dy = {0, 1, -1};
        
        int num = 1;
        int dir = 0;
        int nx = 0, ny = 0,  x = 0, y = 0;
        
        for(int i=0; i<len; ++i){
            map[x][y] = num;
            ++num;
            
            nx = x+dx[dir];
            ny = y+dy[dir];
            
            // 방향 전환 여부 판단
            if(nx < 0 || nx >= n || ny < 0 || ny >= n || map[nx][ny] != 0){
                dir = (dir+1)%3;
                
                nx = x+dx[dir];
                ny = y+dy[dir];
            }
            
            x = nx;
            y = ny;
        }
        
        int idx = 0;
        for(int i=0; i<n; ++i){
            for(int j=0; j<=i; ++j){
                answer[idx] = map[i][j];
                ++idx;
            }
        }
        
        return answer;
    }
}