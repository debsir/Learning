public class Person {

    int age;
    String sex;
    String name;
    static String species;

    Person() {
    }
    
    Person(int age, String sex) {
        this.age = age;
        this.sex = sex;
    }

    Person(int age, String sex, String name) {
        this(age, sex);
        this.name = name;
    }

    void introduce() {
        System.out.println("I am " + species + ".");
    }

    static void die() {
        System.out.println("I am dying! A huge loss of the whole world!");
        System.out.println("This " + species + " is not going to extinct.");
    }

}
