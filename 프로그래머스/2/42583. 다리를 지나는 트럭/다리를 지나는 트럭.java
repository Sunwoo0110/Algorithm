import java.util.*;

class Solution {
    public int solution(int bridge_length, int weight, int[] truck_weights) {
        int answer = 0;
        int totalWeight = 0;
        int idx = 0;
        
        // 다리 위에 올라가 있는 트럭
        Queue<Integer> bridge = new LinkedList<>();
        
        for(int i=0; i<bridge_length; ++i){
            bridge.offer(0);
        }
        
        while(idx<truck_weights.length){
            answer++;
            
            // 맨 앞 트럭 내리기
            totalWeight -= bridge.poll();
            
            if(totalWeight+truck_weights[idx] <= weight) {
                // 트럭 하나 더 올리기
                bridge.offer(truck_weights[idx]);
                totalWeight += truck_weights[idx];
                idx++;
            } else {
                // 무게 초과인 경우, 기존 트럭 하나 씩 이동
                bridge.offer(0);
            }
        }
        
        // 마지막 트럭 내리기
        answer += bridge_length;
        
        return answer;
    }
}