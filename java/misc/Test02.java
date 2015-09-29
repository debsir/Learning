public class Test02 {

    public static void main (String[] args) {
        String A = "rock";
        String B = "paper";
        if (A == B) {
            System.out.println("Tie!");
        } else if (A == "rock" & B == "scissor"
                | A == "scissor" & B == "paper"
                | A == "paper" & B == "rock") {
            System.out.println("A wins!");
        } else {
            System.out.println("B wins!");
        }
    }

}
