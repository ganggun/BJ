import java.util.*;

class Solution {
    public int solution(int a, int b, int c, int d) {
        
        int[] dice = {a, b, c, d};

    
        Map<Integer, Integer> countMap = new HashMap<>();
        for (int num : dice) {
            countMap.put(num, countMap.getOrDefault(num, 0) + 1);
        }


        if (countMap.size() == 1) {
            
            int p = dice[0];
            return 1111 * p;
        } else if (countMap.size() == 2) {
            
            for (int key : countMap.keySet()) {
                int cnt = countMap.get(key);
                if (cnt == 3 || cnt == 1) {
                    // 3개 vs 1개
                    int p = cnt == 3 ? key : getOtherKey(countMap, key);
                    int q = cnt == 1 ? key : getOtherKey(countMap, key);
                    return (int) Math.pow(10 * p + q, 2);
                }
            }

            
            List<Integer> keys = new ArrayList<>(countMap.keySet());
            int p = keys.get(0);
            int q = keys.get(1);
            return (p + q) * Math.abs(p - q);

        } else if (countMap.size() == 3) {
        
            int two = 0;
            int q = 0, r = 0;
            for (int key : countMap.keySet()) {
                int cnt = countMap.get(key);
                if (cnt == 2) {
                    two = key;
                } else if (q == 0) {
                    q = key;
                } else {
                    r = key;
                }
            }
            return q * r;
        } else {
            
            return Arrays.stream(dice).min().getAsInt();
        }
    }


    private int getOtherKey(Map<Integer, Integer> map, int excludeKey) {
        for (int key : map.keySet()) {
            if (key != excludeKey) return key;
        }
        return -1;
    }
}
