public class StarArray {

    public static void main(String[] args) {
        int space = 10;
        for (int row = 1; row <= 11; row++) {
            for (int i = space; i > 0; i--) {
                System.out.print(" ");
            }
            space--;
            for (int j = 1; j <= row; j++) {
                System.out.print("* ");
            }
            System.out.print("\n");
        }
    }

}
