import java.util.Arrays;
import java.util.Scanner;

class Main {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        while (true) {
            int[] arr = new int[3];
            for (int i = 0; i < 3; i++) {
                arr[i]=sc.nextInt();
            }
            Arrays.sort(arr);
            int a= arr[0];
            int b= arr[1];
            int c= arr[2];
            if (arr[0] == 0 && arr[1] == 0 && arr[2] == 0) {
                break;
            }

            if (a*a + b*b ==c*c) {
                System.out.println("right");
            }else {
                System.out.println("wrong");
            }
        }
    }
}
