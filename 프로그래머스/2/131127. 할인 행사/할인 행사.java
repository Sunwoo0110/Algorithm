import java.util.*;

class Solution {
    public int solution(String[] want, int[] number, String[] discount) {
        int answer = 0;
        
        Map<String, Integer> wantMap = new HashMap<>();
        Map<String, Integer> currMap = new HashMap<>();
        
        for(int i=0; i<want.length; ++i){
            wantMap.put(want[i], number[i]);
        }
        
        for(int i=0; i<10; ++i){
            currMap.put(discount[i], currMap.getOrDefault(discount[i], 0)+1);
        }
        
        if(checkContains(wantMap, currMap)) answer++;
        
        // 슬라이딩 윈도우
        for(int i=10; i<discount.length; ++i){
            // 한 칸 밀기
            currMap.put(discount[i-10], currMap.get(discount[i-10])-1); 
            currMap.put(discount[i], currMap.getOrDefault(discount[i], 0)+1);
            
            if(checkContains(wantMap, currMap)) answer++;
        }
        
        return answer;
    }
    
    public boolean checkContains(Map<String, Integer> wantMap, Map<String, Integer> currMap){
        for(Map.Entry<String, Integer> entry: wantMap.entrySet()){
            if(!currMap.containsKey(entry.getKey()) || currMap.get(entry.getKey()) < entry.getValue()) return false;
        }
        
        return true;
    }
}