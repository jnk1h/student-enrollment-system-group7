# Student Enrollment System – Group 7
# Group Members

167141 – Karogo Joe Ndungu

149226 – Patel Radha Shaileshkumar

168869 – Kongo Tressy

150769 – Kibet Yvonne

120406 – Kirui Allan Kiprono

119918 – Fadumo Mohamed

# Project Overview

This project is a Student Enrollment System built with Django REST Framework (DRF). It provides an API for managing students, courses, and enrollments, making it easy to handle academic registration processes.

# Features

Student Management – Add, view, update, and delete student records.

Course Management – Create and manage courses offered by the institution.

Enrollment Management – Enroll students into courses and track registrations.

API Endpoints – RESTful endpoints for Students, Courses, and Enrollments.

Data Validation – Ensures required fields are provided and relationships are valid.

# Project Structure

models.py – Defines Student, Course, and Enrollment models.

serializers.py – Handles data validation and model-to-JSON conversion.

views.py – Uses ModelViewSet for CRUD operations.

urls.py – Configures routes using DRF’s DefaultRouter.

# API Endpoints

Using DRF routers, the following endpoints are available:

Students → /students/

Courses → /courses/

Enrollments → /enrollments/

Each endpoint supports:

GET – Retrieve list or details

POST – Create new record

PUT/PATCH – Update record

DELETE – Remove record

# Setup Instructions

1. Clone the repository:
   cd student-enrollment-system-group7-version2

2. Create and activate a virtual environment:
   python -m venv venv
   venv\Scripts\activate      

3. Install dependencies:
   pip install -r requirements.txt

4. Apply migrations:
   python manage.py makemigrations
   python manage.py migrate

5. Create a superuser:
   python manage.py createsuperuser

6. Run the development server:
   python manage.py runserver

# Testing.

Tests done using Postman.

The system has these 3 groups with the following permissions:<br>
1. Admins - Full access across all models.<br>
2. Lecturers - Can view all models. Can also create and update course.<br>
3. Student - Can only view models.<br>

There are 3 test users belonging to the different groups:<br>
1. allan - Admins<br>
2. User_Lecturer - Lecturers<br>
3. User_Student - Student<br>

Tokens for the 3 users:<br>
![Tokens for 3 users](test-screenshots/Tokens%20for%203%20Users.png)<br>

GET method

GET method test on course:<br>
![DELETE - Result](test-screenshots/DELETE%20-%20Result.png)<br>

POST method

Student trying to add a course:<br>
![POST - Student](test-screenshots/POST%20-%20Student.png)<br>
![POST - Student (2)](test-screenshots/POST%20-%20Student%20(2).png)<br>

Lecturer trying to add a course:<br>
![POST - Lecturer](test-screenshots/POST%20-%20Lecturer.png)<br>
![POST - Lecturer (2)](test-screenshots/POST%20-%20Lecturer%20(2).png)<br>

PUT method

Original data:<br>
![PUT - Original Data](test-screenshots/PUT%20-%20Original%20Data.png)<br>

Lecturer trying to PUT ‘Test Department’:<br>
![PUT - Lecturer](test-screenshots/PUT%20-%20Lecturer.png)<br>
![PUT - Lecturer (2)](test-screenshots/PUT%20-%20Lecturer%20(2).png)<br>

Admin trying to PUT ‘Test Department’:<br>
![PUT - Admin](test-screenshots/PUT%20-%20Admin.png)<br>
![PUT - Admin (2)](test-screenshots/PUT%20-%20Admin%20(2).png)<br>

PATCH method

Admin trying PATCH:<br>
![PATCH - Admin](test-screenshots/PATCH%20-%20Admin.png)<br>
![PATCH - Admin (2)](test-screenshots/PATCH%20-%20Admin%20(2).png)<br>

Student trying PATCH:<br>
![PATCH - Student](test-screenshots/PATCH%20-%20Student.png)<br>
![PATCH - Student (2)](test-screenshots/PATCH%20-%20Student%20(2).png)<br>

DELETE method

Original data:<br>
![DELETE - Original Data](test-screenshots/DELETE%20-%20Original%20Data.png)<br>

Student trying to DELETE instructor:<br>
![DELETE - Student](test-screenshots/DELETE%20-%20Student.png)<br>
![DELETE - Student (2)](test-screenshots/DELETE%20-%20Student%20(2).png)<br>

Lecturer trying to delete instructor:<br>
![DELETE - Lecturer](test-screenshots/DELETE%20-%20Lecturer.png)<br>
![DELETE - Lecturer (2)](test-screenshots/DELETE%20-%20Lecturer%20(2).png)<br>

Admin trying to delete instructor:<br>
![DELETE - Admin](test-screenshots/DELETE%20-%20Admin.png)<br>
![DELETE - Admin (2)](test-screenshots/DELETE%20-%20Admin%20(2).png)<br>

Result of DELETE:<br>
![GET - Admin](test-screenshots/GET%20-%20Admin.png)<br>
