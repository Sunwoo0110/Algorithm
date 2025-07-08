import java.util.*;

class Solution {
    public long solution(int n, int[] works) {
        long answer = 0;
        
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        
        for (int work : works) {
            pq.offer(work);
        }
        
        // 큰 값부터 1씩 줄이기
        while (n > 0 && !pq.isEmpty()) {
            int max = pq.poll();
            if (max > 0) {
                pq.offer(max - 1);
                n--;
            } else {
                break;
            }
        }
        
        while (!pq.isEmpty()) {
            int w = pq.poll();
            answer += (long) w * w;
        }
        
        return answer;
    }
}