import java.util.*;

class Solution {
    public int solution(int[] players, int m, int k) {
        int answer = 0;
        int totalServer = 0;
        int need = 0;
        
        // 작동 중인 서버
        Deque<Integer> queue = new ArrayDeque<>();
        
        for(int i=0; i<players.length; ++i){
            // 작동 시간 끝난 서버 큐에서 제거
            while(!queue.isEmpty()){
                if(i-queue.peekFirst() < k) break;
                queue.pollFirst();                
            }
            
            totalServer = queue.size();
            need = (int) Math.ceil(players[i]/m);
            
            // 서버 증설이 필요한 경우 큐에 추가
            if (need > totalServer) {
                for(int j=0; j<need-totalServer; ++j){
                    queue.addLast(i);
                    answer++;
                }
            }   
        }
         
        return answer;
    }
}