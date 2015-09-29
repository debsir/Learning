class Student extends Person {
    int grade;
    String major;

    Student() {
    }

    void introduce() {
        super.introduce();
        System.out.println("I major in " + major + ".");
        System.out.println("I have got" + grade + ".");
    }
}
