import java.util.*;

class Solution {
    public int[] solution(int[] prices) {
        int[] answer = new int[prices.length];
        
        Deque<Integer> stack = new ArrayDeque<>();
        
        for(int i=prices.length-1; i>=0; --i){
            while(!stack.isEmpty() && prices[i] <= prices[stack.peekLast()]){
                stack.pollLast();
            }
            
            if (!stack.isEmpty()){
                answer[i] = stack.peekLast()-i;
            } else {
                answer[i] = prices.length-1-i;
            }
            
            stack.offerLast(i);
        }
        
        
        return answer;
    }
}