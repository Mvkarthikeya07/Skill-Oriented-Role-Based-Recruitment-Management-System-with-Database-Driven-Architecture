💼 Skill-Based Job & Internship Platform

A Role-Based Recruitment and Application Management System








📌 Overview

The Skill-Based Job & Internship Platform is a database-driven web application designed to connect job seekers and recruiters through a structured, role-based recruitment workflow. The platform enables recruiters to post job opportunities with defined skill requirements, while job seekers can browse listings, apply for positions, and track their application status.

This project demonstrates the practical application of Database Management Systems (DBMS), authentication mechanisms, and IT-enabled recruitment systems using a clean, scalable web architecture.

🎯 Objectives

Design a centralized recruitment management platform

Implement secure user registration and authentication

Support role-based access control (Job Seeker & Recruiter)

Enable job posting, listing, and application workflows

Store and manage recruitment data using a relational database

Apply DBMS and backend concepts in a real-world web system

🚀 Key Features

✔ User registration and login system
✔ Role-based access (Job Seeker / Recruiter)
✔ Recruiter dashboard for posting job opportunities
✔ Job seeker dashboard for browsing and applying to jobs
✔ Skill-based job listings
✔ Application status tracking
✔ Persistent data storage using a relational database
✔ Clean and responsive user interface

🧠 System Design Approach

The application follows a database-centric web architecture with clear separation between presentation, application logic, and data layers.

Core Concepts Applied

Relational Database Design

Authentication and session management

Role-Based Access Control (RBAC)

CRUD operations

Client–server architecture

User Roles

Job Seeker

Register and log in

View available job listings

Apply for jobs

Track application status

Recruiter

Register and log in

Post job openings

View posted job listings

Manage recruitment data

🏗️ Project Structure
skill_based_job_platform/
│
├── static/
│   ├── style.css                   # Application styling
│   └── script.js                   # Client-side scripts
│
├── templates/
│   ├── index.html                  # Landing page
│   ├── register.html               # User registration page
│   ├── login.html                  # User login page
│   ├── dashboard.html              # User dashboard
│   ├── post_job.html               # Job posting page
│   └── apply_job.html              # Job application page
│
├── app.py                          # Flask application entry point
├── database.db                     # SQLite database
│
├── requirements.txt                # Python dependencies
├── LICENSE
└── README.md                       # Project documentation

🔄 Application Workflow

User registers and logs into the system

User role (Job Seeker / Recruiter) is identified

User is redirected to the appropriate dashboard

Recruiters post job openings with skill requirements

Job seekers browse job listings and apply

Application status is stored and updated in the database

🖥️ Application Screenshots
Landing Page

<img width="1366" height="649" alt="Screenshot (66)" src="https://github.com/user-attachments/assets/67f19b70-3d2a-4a37-9784-7b37038a7096" />

Entry point of the platform introducing the skill-based recruitment system.

User Registration

<img width="1366" height="645" alt="Screenshot (65)" src="https://github.com/user-attachments/assets/97bf3db6-9aa9-4df6-9a5f-ca9048c509d3" />

Registration interface allowing users to sign up as Job Seekers or Recruiters.

User Login

<img width="1366" height="649" alt="Screenshot (67)" src="https://github.com/user-attachments/assets/fbf29352-0eac-4320-b36e-da6ca62f029e" />

Secure authentication interface for registered users.

Recruiter – Post a Job

<img width="1366" height="641" alt="Screenshot (70)" src="https://github.com/user-attachments/assets/29907243-5e8b-4a11-bfef-79dfb59f8406" />

Recruiter interface for posting job opportunities with required skills.

Available Jobs – Job Seeker View

<img width="1366" height="653" alt="Screenshot (71)" src="https://github.com/user-attachments/assets/e7e4ddcf-4716-431a-9680-681a91b9dc39" />

Displays job listings along with required skills and application status.

Job Application Status

<img width="1366" height="649" alt="Screenshot (72)" src="https://github.com/user-attachments/assets/15de1ae7-f381-4e6d-acef-d8e4cb35dd2d" />

Shows applied jobs and their current status for job seekers.

⚙️ Installation & Usage
1️⃣ Clone the Repository
git clone <your-repository-url>
cd skill_based_job_platform

2️⃣ Create a Virtual Environment (Optional)
python -m venv venv
source venv/bin/activate      # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
python app.py

5️⃣ Access the Application
http://127.0.0.1:5000

🧪 Technologies Used

Python

Flask

SQLite

HTML

CSS

JavaScript

🔬 Technical Highlights

End-to-end database-driven web application

Secure authentication and role-based workflows

Skill-based job matching logic

Modular and scalable project structure

Real-world recruitment system simulation

🔮 Future Enhancements

Resume upload and profile management

Job recommendation engine

Admin dashboard for system monitoring

Email notifications

Migration to MySQL / PostgreSQL

REST API support

👤 Author

M V Karthikeya
Computer Science Engineer
Interests: Backend Development, Database Systems, Web Applications

GitHub: https://github.com/Mvkarthikeya07

📜 License

This project is licensed under the MIT License.

⭐ Final Remarks

This project demonstrates a well-structured, production-style recruitment management system, showcasing strong understanding of DBMS concepts, backend development, and scalable web application design.
