import java.util.*;

class Solution {
    public int[] solution(int[] fees, String[] records) {
        int[] carNums = {};
        
        // 차량 번호: 들어간 시간
        HashMap<Integer, Integer> carHisMap = new HashMap<>();
        
        // 차량 번호: 누적시간
        TreeMap<Integer, Integer> carTimeMap = new TreeMap<>();
        
        for(int i=0; i<records.length; ++i){
            String[] rec = records[i].split(" ");
            String his = rec[2];
            
            int time = Integer.parseInt(rec[0].split(":")[0])*60 + Integer.parseInt(rec[0].split(":")[1]);
            int carNum = Integer.parseInt(rec[1]);
            
            // 차량 나오는 경우
            if (carHisMap.containsKey(carNum)){
                int totalTime = time-carHisMap.get(carNum);
                
                if (carTimeMap.containsKey(carNum)) {
                    carTimeMap.put(carNum, carTimeMap.get(carNum)+totalTime);
                } else {
                    carTimeMap.put(carNum, totalTime);
                }
                
                carHisMap.remove(carNum);
            }
            
            // 차량 들어오는 경우
            else {
                carHisMap.put(carNum, time);
            }
        }
        
        for (Map.Entry<Integer, Integer> entry : carHisMap.entrySet()) {
            int carNum = entry.getKey();
            int inTime = entry.getValue();
            int outTime = 23 * 60 + 59;  // 23:59
            int totalTime = outTime - inTime;

            if (carTimeMap.containsKey(carNum)) {
                carTimeMap.put(carNum, carTimeMap.get(carNum) + totalTime);
            } else {
                carTimeMap.put(carNum, totalTime);
            }
        }
       
        
        int[] answer = new int[carTimeMap.size()];
        int idx = 0;
        
        for(int totalTime: carTimeMap.values()){
            int totalFare = 0;
                
            // 기본 시간보다 작은 경우
            if (totalTime <= fees[0]){
                answer[idx] = fees[1];
            }
            // 기본 시간보다 큰 경우
            else {
                answer[idx] = fees[1] + (int)Math.ceil((totalTime-fees[0])/(double)fees[2])*fees[3];
            }
            idx++;
        }
        
        return answer;
    }
}