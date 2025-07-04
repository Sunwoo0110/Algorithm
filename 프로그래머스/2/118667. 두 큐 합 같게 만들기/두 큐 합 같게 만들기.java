import java.util.*;

class Solution {
    public int solution(int[] queue1, int[] queue2) {
        int answer = 0;
        long sum1 = 0;
        long sum2 = 0;
        
        Deque<Integer> q1 = new ArrayDeque<>();
        Deque<Integer> q2 = new ArrayDeque<>();
        
        for(int a: queue1){
            sum1 += a;
            q1.addLast(a);
        }
        
        for(int b: queue2){
            sum2 += b;
            q2.addLast(b);
        }
        
        if((sum1+sum2)%2 == 1) return -1; // 합이 홀수면 불가능

        long target = (sum1+sum2)/2;
        int maxLen = 2*(q1.size() + q2.size());
        
        while(answer < maxLen){
            if(sum1 == target) return answer;
            
            if(sum1 > target){
                int out = q1.pollFirst();
                sum1 -= out;
                q2.addLast(out);
                sum2 += out;
            } else {
                int out = q2.pollFirst();
                sum2 -= out;
                q1.addLast(out);
                sum1 += out;
            }
            answer++;
        }
        return -1;
    }
}