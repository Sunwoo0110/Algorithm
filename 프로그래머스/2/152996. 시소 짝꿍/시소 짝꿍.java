import java.util.*;

class Solution {
    public long solution(int[] weights) {
        long answer = 0;
        
        Map<Integer, Long> map = new TreeMap<>();
        for(int w: weights){
            map.put(w, map.getOrDefault(w, (long)0) + 1);
        }
        long cnt = 0;
        for (Map.Entry<Integer, Long> e : map.entrySet()) {
            cnt = e.getValue();
            answer += (cnt*(cnt-1))/2; // nC2
        }
        
        List<Integer> list = new ArrayList<>(map.keySet());
        int n = list.size();
        
        // 완탐
        for(int i=0; i<n; ++i){
            for(int j=i+1; j<n; ++j){
                if(list.get(i)*4 == list.get(j)*2 || list.get(i)*3 == list.get(j)*2 || list.get(i)*4 == list.get(j)*3) { 
                    answer += map.get(list.get(i))*map.get(list.get(j));
                }
            }
        }
        return answer;
    }
}