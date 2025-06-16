import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int l, int r) {

        ArrayList<Integer> list = new ArrayList<Integer>();
        for (int i = l; i < r+1 ; i++) {
            if (q(i)){
                list.add(i);
            }
        }
        if (list.isEmpty()){
            list.add(-1);
        }

        return list;
    }
    public boolean q(int n){
        String s = String.valueOf(n);
        for (char c : s.toCharArray()) {
            if (c != '0' && c != '5') {
                return false;
            }
        }
        return true;
    }
}