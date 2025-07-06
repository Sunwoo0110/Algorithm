import java.util.*;  

class Solution {
    public int solution(int[] topping) {
        int answer = 0;
        
        // 토핑, 해당 토핑 갯수
        Map<Integer, Integer> right = new HashMap<>();
        Set<Integer> left = new HashSet<>();
        
        for(int t: topping){
            right.put(t, right.getOrDefault(t, 0)+1);
        }
        
        for(int t: topping){
            left.add(t);
            
            // right map의 해당 토핑 개수 줄이기
            // 만약 토핑 개수가 0이면 제거
            if(right.containsKey(t)) {
                right.put(t, right.get(t)-1);
                if(right.get(t) == 0) right.remove(t);
            }
            
            if(left.size() == right.size()) answer++;
        }
        
        
        
        return answer;
    }
}