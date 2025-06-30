import java.util.*;

class Solution {
    public String solution(String my_string, int[][] queries) {
        char[] lst = my_string.toCharArray();

        for (int[] q : queries) {
            int start = q[0];
            int end = q[1];

            while (start < end) {
                char temp = lst[start];
                lst[start] = lst[end];
                lst[end] = temp;
                start++;
                end--;
            }
        }

        return new String(lst);
    }
}
