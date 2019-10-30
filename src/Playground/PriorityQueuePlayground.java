package Playground;

import java.util.Objects;
import java.util.PriorityQueue;

public class PriorityQueuePlayground {

    public static void main(String[] args) {

        PriorityQueuePlayground program = new PriorityQueuePlayground();
        program.normalBody();
    }

    public void normalBody() {
        PriorityQueue<Integer> queue = new PriorityQueue<>(5, (a, b) -> {
            if (a%2 == 0) return -1;
            return 0;
//            if (a % 2 == b % 2) Integer.compare(a, b);
//            if (a % 2 == 1 && b % 2 == 0) return -1;
//            return 0;
        });

        queue.add(1);
        queue.add(2);
        queue.add(3);
        queue.add(4);
        queue.add(5);

        for (int n : queue)
            System.out.println(n);
    }



    public void bodyEmployee() {
        PriorityQueue<Employee> queue = new PriorityQueue<>();
        queue.add(new Employee("Old James Stewart", 85000));
        queue.add(new Employee("New James Stewart", 180000));

        for (Employee employee : queue)
            System.out.println(employee.toString());
    }

    class Employee implements Comparable<Employee>{
        String name;
        int salary;

        public Employee(String name, int salary) {
            this.name = name;
            this.salary = salary;
        }

        @Override
        public int compareTo(Employee employee) {
            if (salary > employee.salary) return -1;
            if (salary < employee.salary) return 1;
            return 0;
        }

        @Override
        public boolean equals(Object o) {
            if (this == o) return true;
            if (o == null || o.getClass() != Employee.class) return false;
            Employee employee = (Employee) o;
            return Double.compare(salary, employee.salary) == 0 && Objects.equals(name, employee.name);
        }

        @Override
        public int hashCode() {
            return Objects.hash(name, salary);
        }

        @Override
        public String toString() {
            return "Employee: " + name + " has a salary of $" + salary;
        }
    }
}
