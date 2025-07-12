import java.util.*;

class Solution {
    public int solution(int[] order) {
        int answer = 0;
        int len = order.length;
        
        Deque<Integer> subContainer = new ArrayDeque<>();
        int i = 1;
        
        for(int ord: order){
            if((i != ord && i > len) && (!subContainer.isEmpty() && ord != subContainer.peekLast())){
                break;
            }
            
            while(true){
                if(ord == i){
                    // 바로 트럭에 싣는 경우
                    answer++;
                    i++;
                    break;
                } else if (!subContainer.isEmpty() && ord == subContainer.peekLast()){
                    // 보조 컨테이너에서 싣는 경우
                    subContainer.pollLast();
                    answer++;
                    break;
                } else if (i<=len) {
                    // 순서가 맞지 않아 보조 컨테이너에 보관하는 경우
                    subContainer.offerLast(i);
                    i++;
                } else {
                    // 방법이 없는 경우
                    break;
                }     
            }
        }
        
        
        return answer;
    }
}