# 🎓 Student Course Registration System

A terminal-based relational database project built for **CS4092 – Database Design and Development (Summer 2025)**.

This system simulates a basic university backend where:
- 🧑 Students register for courses
- 👩‍🏫 Instructors teach courses
- 📚 Enrollments are tracked across semesters
- 🧠 SQL queries provide insights into student-course relationships

---

## 🗂️ Tech Stack

- **Database**: PostgreSQL
- **Backend Logic**: Python (CLI-based interface)
- **Schema Design**: ER Modeling → Relational Schema → SQL Implementation
- **Tools Used**: `psycopg2`, `psql`, VS Code

---

## 📁 Project Structure
.
├── student_course_system.sql     # Full schema + sample data
├── cli_app.py                    # Python CLI to interact with DB
├── README.md                     # This file
└── (optional) ER diagram image

## Features
- PostgreSQL schema with 4+ relational tables
- Sample SQL data for testing
- Python CLI interface for interaction
- Multi-table SQL queries for analysis

## How to Run
1. Load the SQL file:
psql -U postgres -d student_registration -f student_course_system.sql

2. Run the Python CLI:
python cli_app.py

## Author
Ishitaa Jain


