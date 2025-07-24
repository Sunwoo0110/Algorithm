import java.util.*;

class Solution {
    public int solution(int[] people, int limit) {
        int answer = 0;
        
        Deque<Integer> dq = new ArrayDeque<>();
        Arrays.sort(people);
        
        for(int p: people){
            dq.addLast(p);
        }
        
        int sum = 0;
        
        while(!dq.isEmpty()){
            sum = dq.pollLast();
            
            if(!dq.isEmpty() && sum+dq.peekFirst() <= limit){
                dq.pollFirst();
            }
            
            answer++;
        }
        
        return answer;
    }
}