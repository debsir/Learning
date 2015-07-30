public class ThisIsGood {

    public static void main(String[] args) {
        Person.species = "animal";
        Person p1 = new Student();
        p1.age = 15;
        p1.sex = "female";
        System.out.println("I am " + p1.age + " years old.");
        p1.introduce();
/*        Person s1 = new Student();
        System.out.println("I am " + s1.species + ".");
        s1.die();
*/
    }

}
