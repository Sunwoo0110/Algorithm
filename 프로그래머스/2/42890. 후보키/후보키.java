import java.util.*;

class Solution {
    public int solution(String[][] relation) {
        int n = relation.length;
        int attrNum = relation[0].length;
        List<Integer> candidateKeys = new ArrayList<>();

        // 비트마스크
        for(int bit=1; bit<(1<<attrNum); bit++) {
            Set<String> set = new HashSet<>();
            
            for (int i=0; i<n; i++) {
                StringBuilder sb = new StringBuilder();
                for (int j=0; j<attrNum; j++) {
                    if ((bit&(1<<j)) != 0) { // j 인덱스 포함할 때
                        sb.append(relation[i][j]).append(",");
                    }
                }
                set.add(sb.toString());
            }

            if (set.size() != n) continue;

            // 최소성 검사
            boolean isMinimal = true;
            for (int key : candidateKeys) {
                if ((key & bit) == key) {
                    isMinimal = false;
                    break;
                }
            }
            if (isMinimal) candidateKeys.add(bit);
        }

        return candidateKeys.size();
    }
}
