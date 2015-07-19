public class Fibonacci {

    public static void main(String[] args) {
        for (int i = 0, int j = 1; i <= 1000; int k = i + j) {
            System.out.println(k);
            i = j;
            j = k;
        }
    }

}

