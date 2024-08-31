public class Main {
    public static void main(String[] args) {
        Student student1 = new Student("arpit", 26, 12);

        Student student1Clone = student1.clone();
        System.out.println(student1Clone.name + " " + student1.name);
    }
} 