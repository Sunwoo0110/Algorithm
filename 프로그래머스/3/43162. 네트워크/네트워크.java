import java.util.*;

class Solution {
    Set<Integer> visited; 
    
    public int solution(int n, int[][] computers) {
        int answer = 0;
        
        visited = new HashSet<>();
        
        for(int i=0; i<n; ++i){
            if(!visited.contains(i)){
                dfs(i, n, computers);
                ++answer;
            }
        }
        
        return answer;
    }
    
    public void dfs(int start, int n, int[][] computers){
        Deque<Integer> queue = new ArrayDeque<>();
        queue.offerLast(start);       

        while(!queue.isEmpty()){
            int cur = queue.pollFirst();
            visited.add(cur);

            for(int i=0; i<n; i++){
                if(cur!=i && computers[cur][i] == 1 && !visited.contains(i)){
                    queue.add(i);
                }
            }
        }
    }
}