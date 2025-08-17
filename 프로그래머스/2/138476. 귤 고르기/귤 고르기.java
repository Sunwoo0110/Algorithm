import java.util.*;

class Solution {
    public int solution(int k, int[] tangerine) {
        int answer = 0;
        
        Map<Integer, Integer> ggulMap = new HashMap<>();
        
        for(int tang: tangerine){
            ggulMap.put(tang, ggulMap.getOrDefault(tang, 0)+1);
        }
        
        List<Map.Entry<Integer, Integer>> list = new ArrayList<>(ggulMap.entrySet());
        list.sort((a, b) -> b.getValue().compareTo(a.getValue()));
        
        for(Map.Entry<Integer, Integer> map: list){
            answer += 1;
            k -= map.getValue();
            
            if(k <= 0){
                break;
            }
        }
        
        return answer;
    }
}