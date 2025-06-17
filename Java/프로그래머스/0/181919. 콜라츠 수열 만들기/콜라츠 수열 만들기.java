import java.util.ArrayList;

class Solution {
    public ArrayList<Integer> solution(int n) {
        ArrayList<Integer> res = new ArrayList<>();

        while (n!=1){
            res.add(n);
            if  (n%2==0){
                n=n/2;
            }
            else{
                n=3*n+1;
            }
        }
        res.add(1);
        return res;
    }
}