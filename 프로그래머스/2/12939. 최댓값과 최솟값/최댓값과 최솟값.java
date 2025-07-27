import java.util.*;

class Solution {
    public String solution(String s) {
        String answer = "";
        String[] strArr = s.split(" ");
        
        int n = strArr.length;
        int[] intArr = new int[n];
        
        for(int i=0; i<n; ++i){
            intArr[i] = Integer.parseInt(strArr[i]);
        }
        
        Arrays.sort(intArr);
        
        answer = intArr[0] + " " + intArr[n-1];
        return answer;
    }
}