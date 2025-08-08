-- Drop existing tables (optional for clean re-runs)
DROP TABLE IF EXISTS Enrollment, Course, Instructor, Student;

-- Table Definitions

CREATE TABLE Student (
  student_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  major VARCHAR(50)
);

CREATE TABLE Instructor (
  instructor_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  department VARCHAR(50)
);

CREATE TABLE Course (
  course_id INT PRIMARY KEY,
  title VARCHAR(100),
  credits INT,
  department VARCHAR(50),
  instructor_id INT,
  FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id)
);

CREATE TABLE Enrollment (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  semester VARCHAR(20),
  grade VARCHAR(2),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- Fixed Instructors
INSERT INTO Instructor VALUES
(101, 'Dr. Hrishikesh Bhide', 'bhideh@ucmail.edu', 'Computer Science'),
(102, 'Dr. Micheal Visloscky', 'vislmi@ucmail.edu', 'Mathematics');

-- Fixed Courses
INSERT INTO Course VALUES
(1001, 'Database Systems', 3, 'Computer Science', 101),
(1002, 'Algorithms', 4, 'Computer Science', 101),
(1003, 'Linear Algebra', 3, 'Mathematics', 102);
