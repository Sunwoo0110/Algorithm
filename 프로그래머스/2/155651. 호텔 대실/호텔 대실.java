import java.util.*;

class Solution {
    public int solution(String[][] book_time) {
        Arrays.sort(book_time, (a, b) -> timeToInt(a[0]) - timeToInt(b[0]));
        
        // 종료 시간 저장
        PriorityQueue<Integer> pq = new PriorityQueue<>();

        for (String[] time : book_time) {
            int start = timeToInt(time[0]);
            int end = timeToInt(time[1]) + 10;

            if (!pq.isEmpty() && pq.peek() <= start) {
                pq.poll(); // 방 재사용 가능
            }

            pq.offer(end); // 새로 배정되거나 재사용된 방의 종료 시각
        }

        return pq.size();
    }

    private int timeToInt(String time) {
        String[] parts = time.split(":");
        return Integer.parseInt(parts[0]) * 60 + Integer.parseInt(parts[1]);
    }
}
