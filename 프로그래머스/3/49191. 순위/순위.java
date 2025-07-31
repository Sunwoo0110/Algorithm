import java.util.*;

class Solution {
    public int solution(int n, int[][] results) {
        int answer = 0;
        
        List<List<Integer>> winGraph = new ArrayList<>();
        List<List<Integer>> loseGraph = new ArrayList<>();
        
        for(int i=0; i<=n; ++i){
            winGraph.add(new ArrayList<>());
            loseGraph.add(new ArrayList<>());
        }
        
        for(int[] res: results){
            winGraph.get(res[0]).add(res[1]);
            loseGraph.get(res[1]).add(res[0]);
        }
        
        for(int i=1; i<=n; ++i){
            boolean[] visited = new boolean[n+1];
            visited[0] = true;
            visited[i] = true;
            
            Deque<Integer> queue = new ArrayDeque<>();
            queue.offerLast(i);
            
            // System.out.println("INDEX: " + i);
            
            while(!queue.isEmpty()){
                int curr = queue.pollFirst();
                visited[curr] = true;
                
                // System.out.println(curr);
                
                for(int next: winGraph.get(curr)){
                    if(visited[next] == false){
                        queue.add(next);
                    }
                }
            }
            
            queue.offerLast(i);
            
            while(!queue.isEmpty()){
                int curr = queue.pollFirst();
                visited[curr] = true;
                
                // System.out.println(curr);
                
                for(int next: loseGraph.get(curr)){
                    if(visited[next] == false){
                        queue.add(next);
                    }
                }
            }
            
            boolean isCertain = true;
            for(boolean b: visited){
                if(!b) {
                    isCertain = false;
                    break;
                }
            }
            
            if(isCertain){
                answer++;
            }
            
        }
        
        return answer;
    }
}