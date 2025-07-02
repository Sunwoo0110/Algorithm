import java.util.*;

class Solution {
    public String solution(int n, int t, int m, int p) {
        StringBuilder answer = new StringBuilder();
        int idx = 0;
        int num = 0;
        p -= 1;
        
        while (true){
            if (answer.length() == t) break;
            
            String binNum = numToBin(num, n);
            
            for(int i=0; i<binNum.length(); ++i){
                if((idx+i)%m == p) {
                    answer.append(binNum.charAt(i));
                
                    if (answer.length() == t) break;
                }
            }
            
            idx += binNum.length();
            num++;
        }
        
        return answer.toString();
    }
    
    public String numToBin(int num, int n){
        if(num == 0) return "0";
        
        StringBuilder result = new StringBuilder();
        
        // charArray 로 num%n 인덱스로 접근하는 방법도 있음
        Map<Integer, String> alp = new HashMap<>();
        alp.put(10, "A");
        alp.put(11, "B");
        alp.put(12, "C");
        alp.put(13, "D");
        alp.put(14, "E");
        alp.put(15, "F");
        
        
        while(num > 0){
            result.append(num%n < 10 ? String.valueOf(num%n) : alp.get(num%n));
            num /= n;
        }
        
        return result.reverse().toString();
    }
}