public class Student implements Prototype{
    String name;
    int age;
    int standard;

    public Student(String name, int age, int standard) {
        this.name = name;
        this.age = age;
        this.standard = standard;
    }

    @Override
    public Student clone() {
        return new Student(name, age, standard);
    }
}
