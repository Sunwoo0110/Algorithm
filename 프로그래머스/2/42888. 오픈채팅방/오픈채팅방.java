import java.util.*;

class Solution {
    public String[] solution(String[] record) {
        List<String> answer = new ArrayList<>();
        
        // 유저 아이디, 닉네임 해시
        Map<String, String> idName = new HashMap<>();
        
        for(String rec: record){
            String[] recArr = rec.split(" ");
            String id = recArr[1];
            
            // 입장인 경우 와 변경인 경우
            if(recArr[0].equals("Enter") || recArr[0].equals("Change")){
                // 기존에 있는 경우 -> 닉네임 변경
                // 새로운 아이디인 경우 -> 추가
                // 변경인 경우
                idName.put(id, recArr[2]);
                
            } 
        }
        
        
        for(String rec: record){
            String[] recArr = rec.split(" ");
            String id = recArr[1];
            
            // 입장인 경우
            if(recArr[0].equals("Enter")) answer.add(idName.get(id) + "님이 들어왔습니다.");  
            else if (recArr[0].equals("Leave")) answer.add(idName.get(id) + "님이 나갔습니다.");  
        }
        
        
        return answer.toArray(new String[0]);
    }
}