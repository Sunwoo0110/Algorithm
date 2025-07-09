class Solution {
    public int[] solution(int n, int s) {
        int[] answer = new int[n];
        int res = 1;
        
        if (n > s) return new int[]{-1};
        
        int target = s/n;
        int remain = s%n;
        
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