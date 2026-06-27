<div align="center">

<h1>💼 Skill-Oriented Role-Based Recruitment Management Syste</h1>
<h3>Database-Driven Architecture · Flask · SQLite · RBAC · Full-Stack Web Application</h3>

<br/>

![Python](https://img.shields.io/badge/Python-3.10+-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Flask](https://img.shields.io/badge/Flask-2.x-000000?style=for-the-badge&logo=flask&logoColor=white)
![SQLite](https://img.shields.io/badge/SQLite-Database-003B57?style=for-the-badge&logo=sqlite&logoColor=white)
![HTML5](https://img.shields.io/badge/HTML5-Frontend-E34F26?style=for-the-badge&logo=html5&logoColor=white)
![CSS3](https://img.shields.io/badge/CSS3-Styling-1572B6?style=for-the-badge&logo=css3&logoColor=white)
![JavaScript](https://img.shields.io/badge/JavaScript-Client--Side-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
![License](https://img.shields.io/badge/License-MIT-green?style=for-the-badge)
![Status](https://img.shields.io/badge/Status-Production--Ready-brightgreen?style=for-the-badge)

<br/>

> **A production-grade, database-driven recruitment platform implementing Role-Based Access Control (RBAC) — connecting job seekers and recruiters through a structured, skill-oriented hiring workflow built with Flask and SQLite.**

<br/>

[![Run Locally](https://img.shields.io/badge/🚀_Run_Locally-Flask_App-darkblue?style=for-the-badge)](#️-installation--usage)
[![GitHub](https://img.shields.io/badge/GitHub-Mvkarthikeya07-181717?style=for-the-badge&logo=github)](https://github.com/Mvkarthikeya07)

</div>

---

## 📑 Table of Contents

- [Overview](#-overview)
- [Live Screenshots](#️-live-screenshots)
- [System Design & Architecture](#-system-design--architecture)
- [Role-Based Access Control](#-role-based-access-control-rbac)
- [Database Schema Design](#️-database-schema-design)
- [Application Workflow](#-application-workflow)
- [Project Structure](#️-project-structure)
- [Installation & Usage](#️-installation--usage)
- [Tech Stack](#-tech-stack)
- [Technical Highlights](#-technical-highlights)
- [Future Roadmap](#-future-roadmap)
- [Author](#-author)

---

## 🧭 Overview

The **Skill-Oriented Role-Based Recruitment Management System** is a full-stack, database-centric web application that digitizes the end-to-end hiring pipeline. It bridges the gap between job seekers and recruiters through a structured, role-aware workflow — where every user action is governed by their assigned role and persisted in a relational database.

This project demonstrates practical mastery of:

| Concept | Application |
|---------|-------------|
| 🗄️ **DBMS** | Relational schema design, CRUD operations, SQLite |
| 🔐 **Authentication** | Secure registration, login, session management |
| 👥 **RBAC** | Role-based dashboards and access control |
| 🌐 **Full-Stack Dev** | Flask backend + Jinja2 templates + JS/CSS frontend |
| 🏗️ **Architecture** | 3-tier: Presentation → Application Logic → Data Layer |
| 📋 **Workflow Engine** | Job posting → Application → Status tracking pipeline |

---

## 🖥️ Live Screenshots

### 🔸 Landing Page

<div align="center">
<img width="900" alt="Landing Page" src="https://github.com/user-attachments/assets/67f19b70-3d2a-4a37-9784-7b37038a7096" />

*Entry point of the platform — introduces the skill-based recruitment system and routes users to register or login.*
</div>

---

### 🔸 User Registration

<div align="center">
<img width="900" alt="User Registration" src="https://github.com/user-attachments/assets/97bf3db6-9aa9-4df6-9a5f-ca9048c509d3" />

*Registration interface — users sign up and select their role (Job Seeker or Recruiter), which governs their entire platform experience.*
</div>

---

### 🔸 User Login

<div align="center">
<img width="900" alt="User Login" src="https://github.com/user-attachments/assets/fbf29352-0eac-4320-b36e-da6ca62f029e" />

*Secure authentication interface — credentials validated against the database, session initialized on success.*
</div>

---

### 🔸 Recruiter — Post a Job

<div align="center">
<img width="900" alt="Recruiter Post Job" src="https://github.com/user-attachments/assets/29907243-5e8b-4a11-bfef-79dfb59f8406" />

*Recruiter-exclusive dashboard — post job openings with title, description, required skills, and eligibility criteria.*
</div>

---

### 🔸 Job Seeker — Available Jobs View

<div align="center">
<img width="900" alt="Available Jobs View" src="https://github.com/user-attachments/assets/e7e4ddcf-4716-431a-9680-681a91b9dc39" />

*Job seeker dashboard — browse all active listings with required skills and one-click application submission.*
</div>

---

### 🔸 Job Application Status Tracker

<div align="center">
<img width="900" alt="Application Status Tracker" src="https://github.com/user-attachments/assets/15de1ae7-f381-4e6d-acef-d8e4cb35dd2d" />

*Personalized status tracker — shows all jobs applied to and their current recruitment status in real time.*
</div>

---

## 🏗️ System Design & Architecture

This project follows a clean **3-tier architecture** with strict separation between layers:

```
┌─────────────────────────────────────────────────┐
│              PRESENTATION LAYER                 │
│   HTML5 Templates (Jinja2) · CSS3 · JavaScript  │
│   index, register, login, dashboard,            │
│   post_job, apply_job pages                     │
└───────────────────────┬─────────────────────────┘
                        │ HTTP Request / Response
                        ▼
┌─────────────────────────────────────────────────┐
│            APPLICATION LOGIC LAYER              │
│              Flask (app.py)                     │
│  ├─ Route handling & URL dispatch               │
│  ├─ Session management & authentication         │
│  ├─ Role-based access control enforcement       │
│  ├─ Business logic (job posting, applying)      │
│  └─ Input validation & form processing          │
└───────────────────────┬─────────────────────────┘
                        │ SQL Queries
                        ▼
┌─────────────────────────────────────────────────┐
│                  DATA LAYER                     │
│              SQLite (database.db)               │
│  ├─ Users table (id, name, email, role, hash)   │
│  ├─ Jobs table (id, title, skills, recruiter)   │
│  └─ Applications table (user_id, job_id, status)│
└─────────────────────────────────────────────────┘
```

---

## 👥 Role-Based Access Control (RBAC)

The platform enforces strict role-based routing — users can only access pages and actions permitted by their assigned role:

| Feature / Action | 🧑‍💼 Job Seeker | 👔 Recruiter |
|-----------------|:--------------:|:------------:|
| Register & Login | ✅ | ✅ |
| View Job Listings | ✅ | ✅ |
| Apply for Jobs | ✅ | ❌ |
| Track Application Status | ✅ | ❌ |
| Post Job Openings | ❌ | ✅ |
| View Posted Jobs | ❌ | ✅ |
| Manage Job Listings | ❌ | ✅ |
| View Applicants | ❌ | ✅ |

> **RBAC is enforced server-side** — Flask route decorators check session role before serving any restricted page, preventing unauthorized access regardless of URL manipulation.

---

## 🗃️ Database Schema Design

The application uses a **normalized relational schema** with 3 core tables:

```
┌──────────────────────┐       ┌──────────────────────────┐
│        USERS         │       │          JOBS            │
│──────────────────────│       │──────────────────────────│
│ id (PK)              │       │ id (PK)                  │
│ name                 │       │ title                    │
│ email (UNIQUE)       │       │ description              │
│ password_hash        │       │ required_skills          │
│ role (seeker/recruit)│       │ recruiter_id (FK→users)  │
│ created_at           │       │ posted_at                │
└──────────┬───────────┘       └────────────┬─────────────┘
           │                                │
           │         ┌──────────────────────┘
           │         │
           ▼         ▼
┌──────────────────────────────┐
│         APPLICATIONS         │
│──────────────────────────────│
│ id (PK)                      │
│ user_id (FK → users)         │
│ job_id  (FK → jobs)          │
│ status (pending/reviewed/    │
│         accepted/rejected)   │
│ applied_at                   │
└──────────────────────────────┘
```

**Key design decisions:**
- Passwords stored as **hashed values** — never plaintext
- `role` field drives all RBAC logic at the application layer
- `UNIQUE` constraint on email prevents duplicate registrations
- Foreign keys maintain **referential integrity** between users, jobs, and applications

---

## 🔄 Application Workflow

```
User Visits Platform
        │
        ▼
┌─────────────────────┐
│  Register / Login   │  ← Role selected at registration
└────────┬────────────┘
         │
    ┌────┴────┐
    │         │
    ▼         ▼
Job Seeker  Recruiter
Dashboard   Dashboard
    │         │
    │         ▼
    │   Post Job Opening
    │   (title, skills, desc)
    │         │
    │         ▼
    │   Job stored in DB
    │
    ▼
Browse Available Jobs
    │
    ▼
Apply for Job (one-click)
    │
    ▼
Application stored in DB
(status: Pending)
    │
    ▼
Track Status on Dashboard
(Pending → Reviewed → Accepted/Rejected)
```

---

## 🏗️ Project Structure

```
skill_based_job_platform/
│
├── 📁 static/
│   ├── style.css                   # Application-wide CSS styling
│   └── script.js                   # Client-side interactivity
│
├── 📁 templates/
│   ├── index.html                  # Landing page
│   ├── register.html               # Role-selection registration form
│   ├── login.html                  # Secure authentication page
│   ├── dashboard.html              # Role-aware user dashboard
│   ├── post_job.html               # Recruiter — job posting form
│   └── apply_job.html              # Job seeker — application form
│
├── 📄 app.py                       # Flask app — routes, auth, RBAC, DB logic
├── 🗄️ database.db                  # SQLite relational database
│
├── 📄 requirements.txt             # Python dependencies
├── 📄 LICENSE                      # MIT License
└── 📄 README.md                    # Project documentation
```

---

## ⚙️ Installation & Usage

### Prerequisites
- Python 3.10+
- pip

### 1️⃣ Clone the Repository

```bash
git clone https://github.com/Mvkarthikeya07/Skill-Oriented-Role-Based-Recruitment-Management-System.git
cd skill_based_job_platform
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # macOS / Linux
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Run the Application

```bash
python app.py
```

### 5️⃣ Access in Browser

```
http://127.0.0.1:5000
```

> The SQLite database (`database.db`) is auto-created on first run — no separate DB setup required.

---

## 🛠️ Tech Stack

<div align="center">

| Layer | Technology | Purpose |
|-------|-----------|---------|
| **Language** | Python 3.10+ | Core backend development |
| **Web Framework** | Flask | Routes, sessions, auth, RBAC |
| **Database** | SQLite | Relational data storage & queries |
| **ORM / DB Layer** | Flask-SQLAlchemy / sqlite3 | Database interaction |
| **Templating** | Jinja2 | Server-side HTML rendering |
| **Frontend** | HTML5, CSS3, JavaScript | UI, forms, client-side logic |
| **Security** | Werkzeug / hashlib | Password hashing |

</div>

---

## 🔬 Technical Highlights

- **3-tier architecture** — clean separation of presentation, logic, and data layers
- **Server-side RBAC enforcement** — role checked on every protected route, not just UI
- **Normalized relational schema** — 3-table design with foreign keys and referential integrity
- **Secure authentication** — passwords hashed before storage, never stored in plaintext
- **Session-based state management** — Flask sessions track authenticated user and role
- **Full CRUD implementation** — Create, Read, Update, Delete across jobs and applications
- **Skill-based filtering** — job listings tagged with required skills for targeted discovery
- **Zero external DB dependency** — SQLite runs embedded, no server setup needed

---

## 🔮 Future Roadmap

- [ ] 📄 **Resume Upload** — PDF/DOCX upload and profile management for job seekers
- [ ] 🤖 **Job Recommendation Engine** — ML-based skill-to-job matching (cosine similarity / TF-IDF)
- [ ] 🛡️ **Admin Dashboard** — System-wide monitoring, user management, analytics
- [ ] 📧 **Email Notifications** — Status update alerts via SMTP / SendGrid
- [ ] 🗄️ **PostgreSQL Migration** — Scale from SQLite to production-grade relational DB
- [ ] 🔌 **REST API** — Expose endpoints for mobile app or third-party integration
- [ ] 🐳 **Dockerization** — Containerize for portable cloud deployment
- [ ] ☁️ **Cloud Deployment** — Host on Render / Railway / AWS EC2

---

## 👤 Author

<div align="center">

**M V Karthikeya**
*Computer Science Engineer | Backend Development · Database Systems · Web Applications*

[![GitHub](https://img.shields.io/badge/GitHub-Mvkarthikeya07-181717?style=for-the-badge&logo=github)](https://github.com/Mvkarthikeya07)

</div>

---

## 📜 License

This project is licensed under the **MIT License** — see the [LICENSE](LICENSE) file for details.

---

<div align="center">

**⭐ If this project helped you, star the repo — it means a lot!**

*Architected with purpose. Secured by design. Built to scale.*

</div>
