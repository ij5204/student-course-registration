-- DROP TABLES if they exist (optional for clean runs)
DROP TABLE IF EXISTS Enrollment, Course, Instructor, Student;

-- 1. Student Table
CREATE TABLE Student (
  student_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  major VARCHAR(50)
);

-- 2. Instructor Table
CREATE TABLE Instructor (
  instructor_id INT PRIMARY KEY,
  name VARCHAR(100),
  email VARCHAR(100),
  department VARCHAR(50)
);

-- 3. Course Table
CREATE TABLE Course (
  course_id INT PRIMARY KEY,
  title VARCHAR(100),
  credits INT,
  department VARCHAR(50),
  instructor_id INT,
  FOREIGN KEY (instructor_id) REFERENCES Instructor(instructor_id)
);

-- 4. Enrollment Table
CREATE TABLE Enrollment (
  enrollment_id INT PRIMARY KEY,
  student_id INT,
  course_id INT,
  semester VARCHAR(20),
  grade VARCHAR(2),
  FOREIGN KEY (student_id) REFERENCES Student(student_id),
  FOREIGN KEY (course_id) REFERENCES Course(course_id)
);

-- ----------------------------------
-- 🔹 Sample Data Inserts
-- ----------------------------------

-- Students
INSERT INTO Student VALUES
(1, 'Alice Smith', 'alice@example.com', 'Computer Science'),
(2, 'Bob Johnson', 'bob@example.com', 'Information Systems'),
(3, 'Charlie Lee', 'charlie@example.com', 'Data Science');

-- Instructors
INSERT INTO Instructor VALUES
(101, 'Dr. Hrishikesh Bhide', 'bhideh@ucmail.edu', 'Computer Science'),
(102, 'Dr. Micheal Visloscky', 'vislmi@ucmail.edu', 'Mathematics');

-- Courses
INSERT INTO Course VALUES
(1001, 'Database Systems', 3, 'Computer Science', 101),
(1002, 'Algorithms', 4, 'Computer Science', 101),
(1003, 'Linear Algebra', 3, 'Mathematics', 102);

-- Enrollments
INSERT INTO Enrollment VALUES
(201, 1, 1001, 'Fall 2025', 'A'),
(202, 1, 1002, 'Fall 2025', 'B+'),
(203, 2, 1001, 'Fall 2025', 'A-'),
(204, 3, 1003, 'Fall 2025', 'B');
