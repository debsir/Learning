public class ThisIsGood {

    public static void main(String[] args) {
        Person.die();
        Person.species = "animal";
        Person p1 = new Person(15, "female");
        System.out.println("I am " + p1.age + " years old.");
        Person s1 = new Student();
        System.out.println("I am " + s1.species + ".");
        s1.die();
    }

}
