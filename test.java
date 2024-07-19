final class Employee {
    int x = 10;
}

public class test {
    public static void main(String args[]) {
        Employee obj1 = new Employee();
        Employee obj2 = new Employee();
        System.out.println("Actual value = " + obj1.x);
        System.out.println("Actual value = " + obj2.x);
        modifyX(obj1);
        System.out.println("After modifying = " + obj1.x);
        System.out.println("After modifying = " + obj2.x);
    }

    private static void modifyX(Employee emp){
        emp.x = 20;
    }
}