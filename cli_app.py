import psycopg2

# Establish DB connection
conn = psycopg2.connect(
    dbname="student_registration",
    user="postgres",
    password="Password@5204",
    host="localhost",
    port="5432"
)
cur = conn.cursor()

def add_student():
    sid = int(input("Student ID: "))
    name = input("Name: ")
    email = input("Email: ")
    major = input("Major: ")
    cur.execute("INSERT INTO Student VALUES (%s, %s, %s, %s)", (sid, name, email, major))
    conn.commit()
    print("Student added.\n")

def view_courses():
    cur.execute("SELECT course_id, title FROM Course")
    for row in cur.fetchall():
        print(f"{row[0]} - {row[1]}")
    print()

def enroll_student():
    eid = int(input("Enrollment ID: "))
    sid = int(input("Student ID: "))
    cid = int(input("Course ID: "))
    sem = input("Semester (e.g., Fall 2025): ")
    grade = input("Grade (or NULL): ") or None
    cur.execute("INSERT INTO Enrollment VALUES (%s, %s, %s, %s, %s)", (eid, sid, cid, sem, grade))
    conn.commit()
    print("Enrolled\n")

def view_enrollments():
    cur.execute("""
        SELECT s.name, c.title, e.semester, e.grade
        FROM Enrollment e
        JOIN Student s ON s.student_id = e.student_id
        JOIN Course c ON c.course_id = e.course_id
    """)
    for row in cur.fetchall():
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()

def view_full_enrollments():
    cur.execute("""
        SELECT s.name, c.title, e.semester, e.grade
        FROM Enrollment e
        JOIN Student s ON s.student_id = e.student_id
        JOIN Course c ON c.course_id = e.course_id;
    """)
    for row in cur.fetchall():
        print(f"{row[0]} | {row[1]} | {row[2]} | {row[3]}")
    print()

def view_courses_with_instructors():
    cur.execute("""
        SELECT c.title, i.name
        FROM Course c
        JOIN Instructor i ON c.instructor_id = i.instructor_id;
    """)
    for row in cur.fetchall():
        print(f"{row[0]} taught by {row[1]}")
    print()

def view_courses_for_student():
    name = input("Enter student name: ")
    cur.execute("""
        SELECT c.title, e.semester
        FROM Enrollment e
        JOIN Student s ON s.student_id = e.student_id
        JOIN Course c ON c.course_id = e.course_id
        WHERE s.name = %s;
    """, (name,))
    rows = cur.fetchall()
    if not rows:
        print("No courses found for that student.\n")
    else:
        for row in rows:
            print(f"{row[0]} | {row[1]}")
        print()

def count_courses_per_student():
    cur.execute("""
        SELECT s.name, COUNT(e.course_id)
        FROM Student s
        JOIN Enrollment e ON s.student_id = e.student_id
        GROUP BY s.name;
    """)
    for row in cur.fetchall():
        print(f"{row[0]}: {row[1]} courses")
    print()

def find_unenrolled_students():
    cur.execute("""
        SELECT s.name
        FROM Student s
        LEFT JOIN Enrollment e ON s.student_id = e.student_id
        WHERE e.enrollment_id IS NULL;
    """)
    for row in cur.fetchall():
        print(f"{row[0]} is not enrolled in any course.")
    print()


def main():
    while True:
        print("=== Student Course Registration System ===")
        print("1. Add Student")
        print("2. View Courses")
        print("3. Enroll Student")
        print("4. View Enrollments")
        print("5. Find Students Not Enrolled in Any Course")
        print("6. View Full Enrollments (Student + Course + Grade)")
        print("7. View Courses with Instructors")
        print("8. View Courses for a Student")
        print("9. Count Courses per Student")
        print("10. Exit" )

        choice = input("Select option: ")
        
        if choice == '1':
            add_student()
        elif choice == '2':
            view_courses()
        elif choice == '3':
            enroll_student()
        elif choice == '4':
            view_enrollments()
        elif choice == '5':
            find_unenrolled_students()
        elif choice == '6':
            view_full_enrollments()
        elif choice == '7':
            view_courses_with_instructors()
        elif choice == '8':
            view_courses_for_student()
        elif choice == '9':
            count_courses_per_student()
        elif choice == '10':
            break
        else:
            print("❌ Invalid option\n")

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
