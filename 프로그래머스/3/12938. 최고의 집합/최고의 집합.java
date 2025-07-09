class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        
        if (n > s) return new int[]{-1};
        
        int target = s/n;
        int remain = s%n;
        
        // 최대한 차이가 적은 숫자들이 집합이 이루어야 함
        for(int i=n-1; i>=0; --i){
            if (remain <= 0){
                answer[i] = target;
            } 
            else {
                answer[i] = target+1;
                remain--;
            }
        }
        
        return answer;
    }
}