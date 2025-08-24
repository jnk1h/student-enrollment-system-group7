Testing.

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
![GET - Admin](test-screenshots/GET%20-%20Admin.png)<br>

POST method

When a student tries to add a course:<br>
![POST - Student](test-screenshots/POST%20-%20Student.png)<br>
![POST - Student (2)](test-screenshots/POST%20-%20Student%20(2).png)<br>

A teacher trying to add a course:<br>
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
![PUT - Original Data](test-screenshots/PUT%20-%20Original%20Data.png)<br>

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
![DELETE - Result](test-screenshots/DELETE%20-%20Result.png)<br>
