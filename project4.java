import java.util.*;
import java.io.*;

// Interfaces
interface StudentInterface {
    int getStudentID();
    String getFirstName();
    String getLastName();
    String getLevel();
    boolean isActive();
    void setActive(boolean active);
    void display();
}

interface CourseInterface {
    int getCourseID();
    String getCourseName();
}

// Student class
class Student implements StudentInterface {
    int studentID;
    String firstName;
    String lastName;
    String level;
    boolean isActive;

    Student(int studentID, String firstName, String lastName, String level) {
        this.studentID = studentID;
        this.firstName = firstName;
        this.lastName = lastName;
        this.level = level;
        this.isActive = true;
    }

    // Implement StudentInterface methods
    public int getStudentID() { return studentID; }
    public String getFirstName() { return firstName; }
    public String getLastName() { return lastName; }
    public String getLevel() { return level; }
    public boolean isActive() { return isActive; }
    public void setActive(boolean active) { isActive = active; }

    // Display student information
    public void display() {
        System.out.println(firstName + " " + lastName);
        System.out.println("ID: " + studentID);
        System.out.println("Level: " + level);
        System.out.println("Status: " + (isActive ? "Active" : "Inactive"));
    }
}

// Student_Employee class
class Student_Employee extends Student {
    String employmentType;
    String job;

    Student_Employee(int studentID, String firstName, String lastName, String level, String employmentType, String job) {
        super(studentID, firstName, lastName, level);
        this.employmentType = employmentType;
        this.job = job;
    }

    // Display student job details
    void displayJobDetails() {
        display();
        System.out.println("Employment Type: " + employmentType);
        System.out.println("Job: " + job);
    }
}

// Course class
class Course implements CourseInterface {
    int courseID;
    String courseName;

    Course(int courseID, String courseName) {
        this.courseID = courseID;
        this.courseName = courseName;
    }

    // Implement CourseInterface methods
    public int getCourseID() { return courseID; }
    public String getCourseName() { return courseName; }
}

// Main class
public class AditPathania_Section501_Project4 {
    static List<Student> students = new ArrayList<>();
    static List<Student_Employee> studentEmployees = new ArrayList<>();
    static List<Course> courses = new ArrayList<>();
    static int nextStudentID = 0;

    public static void main(String[] args) {
        Scanner scanner = new Scanner(System.in);

        System.out.println("Welcome to Student and Course Management System!");

        // Main menu loop
        while (true) {
            // Display main menu options
            System.out.println("\n***Main Menu***");
            System.out.println("Press '1' for Student Management System (SMS)");
            System.out.println("Press '2' for Course Management System (CMS)");
            System.out.println("Press '0' to exit");
            System.out.print("Select an option: ");

            int choice = scanner.nextInt();

            if (choice == 1) {
                studentManagementSystem(scanner);
            } else if (choice == 2) {
                courseManagementSystem(scanner);
            } else if (choice == 0) {
                System.out.println("Good Bye!!!");
                break;
            } else {
                System.out.println("Invalid choice, try again.");
            }
        }

        scanner.close();
    }

    // SMS menu
    private static void studentManagementSystem(Scanner scanner) {
        while (true) {
            System.out.println("\n***Welcome to SMS***");
            System.out.println("\nPress '1' to add a student");
            System.out.println("Press '2' to deactivate a student");
            System.out.println("Press '3' to display all students");
            System.out.println("Press '4' to search for a student by ID");
            System.out.println("Press '5' to assign on-campus job");
            System.out.println("Press '6' to display all students with on-campus jobs");
            System.out.println("Press '0' to exit SMS");
            System.out.print("Select an option: ");

            int smsChoice = scanner.nextInt();
            scanner.nextLine();

            // Handle SMS menu options
            if (smsChoice == 1) {
                addStudent(scanner);
            } else if (smsChoice == 2) {
                deactivateStudent(scanner);
            } else if (smsChoice == 3) {
                displayAllStudents();
            } else if (smsChoice == 4) {
                searchStudentByID(scanner);
            } else if (smsChoice == 5) {
                assignOnCampusJob(scanner);
            } else if (smsChoice == 6) {
                displayStudentEmployees();
            } else if (smsChoice == 0) {
                return;
            } else {
                System.out.println("Invalid choice. Please try again.");
            }
        }
    }

    // Add a student
    private static void addStudent(Scanner scanner) {
        System.out.print("Enter first name: ");
        String firstName = scanner.nextLine();

        System.out.print("Enter last name: ");
        String lastName = scanner.nextLine();

        System.out.print("Enter level of the student: ");
        String level = scanner.nextLine();

        // Create a new student and add it to the students list
        Student newStudent = new Student(nextStudentID++, firstName, lastName, level);
        students.add(newStudent);

        System.out.println(firstName + " " + lastName + " has been added as a " + level + " with ID " + newStudent.studentID);
    }

    // Deactivate a student
    private static void deactivateStudent(Scanner scanner) {
        System.out.print("Enter the ID for the student you want to deactivate: ");
        int id = scanner.nextInt();

        // Iterate through students and deactivate the one with the given ID
        for (Student s : students) {
            if (s.studentID == id) {
                s.setActive(false);
                System.out.println(s.firstName + " " + s.lastName + " has been deactivated.");
                return;
            }
        }

        System.out.println("Student with ID " + id + " not found.");
    }

    // Display all active students
    private static void displayAllStudents() {
        for (Student s : students) {
            if (s.isActive()) {
                s.display();
            }
        }
    }

    // Search for a student by ID
    private static void searchStudentByID(Scanner scanner) {
        System.out.print("Enter the student ID: ");
        int studentID = scanner.nextInt();

        // Iterate through students and display the one with the given ID if it's active
        for (Student s : students) {
            if (s.studentID == studentID && s.isActive()) {
                s.display();
                return;
            }
        }

        System.out.println("Student with ID " + studentID + " not found or is inactive.");
    }

    // Assign an on-campus job to a student
    private static void assignOnCampusJob(Scanner scanner) {
        System.out.print("Enter student ID: ");
        int studentID = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter job: ");
        String job = scanner.nextLine();

        System.out.print("Enter job type: ");
        String employmentType = scanner.nextLine();

        Student student = null;
        // Find the student with the given ID
        for (Student s : students) {
            if (s.studentID == studentID && s.isActive()) {
                student = s;
                break;
            }
        }

        // If the student is not found or inactive, display an error message
        if (student == null) {
            System.out.println("Student with ID " + studentID + " not found or is inactive.");
            return;
        }

        // Create a new student employee and add it to the studentEmployees list
        Student_Employee employee = new Student_Employee(student.studentID, student.firstName, student.lastName, student.level, employmentType, job);
        studentEmployees.add(employee);

        System.out.println(student.firstName + " " + student.lastName + " has been assigned " + employmentType + " " + job + " job");
    }

    // Display all students with on-campus jobs
    private static void displayStudentEmployees() {
        System.out.println("Students with on-campus jobs:");
        for (Student_Employee employee : studentEmployees) {
            System.out.println("ID - " + employee.studentID);
            System.out.println(employee.firstName + " " + employee.lastName);
            System.out.println(employee.employmentType + " " + employee.job);
            System.out.println();
        }
    }

    // CMS menu
    private static void courseManagementSystem(Scanner scanner) {
        while (true) {
            System.out.println("\n***Welcome to CMS***");
            System.out.println("\nPress '1' to add a new course");
            System.out.println("Press '2' to assign student a new course");
            System.out.println("Press '3' to display student with assigned courses");
            System.out.println("Press '0' to exit CMS");
            System.out.print("Select an option: ");

            int cmsChoice = scanner.nextInt();
            scanner.nextLine();

            // Handle CMS menu options
            if (cmsChoice == 1) {
                addCourse(scanner);
            } else if (cmsChoice == 2) {
                assignCourseToStudent(scanner);
            } else if (cmsChoice == 3) {
                displayStudentsWithCourses();
            } else if (cmsChoice == 0) {
                return;
            } else {
                System.out.println("Invalid choice, please try again.");
            }
        }
    }

    // Add a course
    private static void addCourse(Scanner scanner) {
        System.out.print("Enter course ID: ");
        int courseID = scanner.nextInt();
        scanner.nextLine();

        System.out.print("Enter course name: ");
        String courseName = scanner.nextLine();

        // Create a new course and add it to the courses list
        Course newCourse = new Course(courseID, courseName);
        courses.add(newCourse);

        System.out.println("Confirmation: New course " + courseID + " has been added");
    }

    // Assign a course to a student
    private static void assignCourseToStudent(Scanner scanner) {
        System.out.print("Enter student ID: ");
        int studentID = scanner.nextInt();

        System.out.print("Enter course ID: ");
        int courseID = scanner.nextInt();

        Student student = null;
        // Find the student with the given ID
        for (Student s : students) {
            if (s.studentID == studentID && s.isActive()) {
                student = s;
                break;
            }
        }

        if (student == null) {
            System.out.println("Student with ID " + studentID + " not found or is inactive.");
            return;
        }

        Course course = null;
        // Find the course with the given ID
        for (Course c : courses) {
            if (c.courseID == courseID) {
                course = c;
                break;
            }
        }

        if (course == null) {
            System.out.println("Course with ID " + courseID + " not found.");
            return;
        }

        System.out.println("Confirmation: " + student.firstName + " " + student.lastName + " has been assigned course " + courseID);
    }

    // Display students with assigned courses
    private static void displayStudentsWithCourses() {
        for (Student s : students) {
            if (s.isActive()) {
                System.out.println(s.firstName + " " + s.lastName);
                System.out.println("ID – " + s.studentID);
                System.out.print("Courses: ");
                System.out.println();
            }
        }
    }
}