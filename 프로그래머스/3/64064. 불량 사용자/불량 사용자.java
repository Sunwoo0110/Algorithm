import java.util.*;

class Solution {
    Set<Set<String>> answerSet = new HashSet<>();

    public int solution(String[] user_id, String[] banned_id) {
        int answer = 0;
        
        List<List<String>> candidates = new ArrayList<>();
        for (String ban: banned_id) {
            List<String> can = new ArrayList<>();
            for (String user : user_id) {
                if (isMatch(user, ban)) can.add(user);
            }
            candidates.add(can);
        }

        dfs(candidates, 0, new HashSet<>());
        return answerSet.size();
    }

    // 백트래킹
    void dfs(List<List<String>> candidates, int depth, Set<String> curr) {
        if (depth == candidates.size()) {
            answerSet.add(new HashSet<>(curr));
            return;
        }
        
        for (String user: candidates.get(depth)) {
            if (!curr.contains(user)) {
                curr.add(user);
                dfs(candidates, depth+1, curr);
                curr.remove(user);
            }
        }
    }

    boolean isMatch(String user, String ban) {
        if (user.length() != ban.length()) return false;
        for (int i=0; i < user.length(); i++) {
            if (ban.charAt(i) != '*' && user.charAt(i) != ban.charAt(i))
                return false;
        }
        return true;
    }
}
