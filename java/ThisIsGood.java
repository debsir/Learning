public class ThisIsGood {

    public static void main(String[] args) {
        Person.die();
        Person.species = "animal";
        Person p1 = new Person(15, "female");
        System.out.println("I am " + p1.age + " years old.");
        Person p2 = new Person();
        System.out.println("I am " + p2.species + ".");
        p2.die();
    }

}
