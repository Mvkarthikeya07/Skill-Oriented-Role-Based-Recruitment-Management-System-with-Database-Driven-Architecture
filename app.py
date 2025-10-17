# app.py
from flask import Flask, render_template, request, redirect, url_for, session
import sqlite3

app = Flask(__name__)
app.secret_key = "your_secret_key"

DB_NAME = "database.db"

# ---------------------------
# Initialize Database
# ---------------------------
def init_db():
    with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
        c = conn.cursor()
        # Users table
        c.execute('''CREATE TABLE IF NOT EXISTS users (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     name TEXT NOT NULL,
                     email TEXT UNIQUE NOT NULL,
                     password TEXT NOT NULL,
                     role TEXT NOT NULL)''')
        # Jobs table
        c.execute('''CREATE TABLE IF NOT EXISTS jobs (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     title TEXT NOT NULL,
                     description TEXT NOT NULL,
                     skills TEXT NOT NULL,
                     recruiter_id INTEGER NOT NULL,
                     FOREIGN KEY(recruiter_id) REFERENCES users(id))''')
        # Applications table
        c.execute('''CREATE TABLE IF NOT EXISTS applications (
                     id INTEGER PRIMARY KEY AUTOINCREMENT,
                     job_id INTEGER NOT NULL,
                     user_id INTEGER NOT NULL,
                     FOREIGN KEY(job_id) REFERENCES jobs(id),
                     FOREIGN KEY(user_id) REFERENCES users(id))''')
        conn.commit()

init_db()

# ---------------------------
# Routes
# ---------------------------

# Home Page
@app.route('/')
def index():
    return render_template('index.html')

# Register
@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        password = request.form['password']
        role = request.form['role']

        try:
            with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
                c = conn.cursor()
                c.execute("INSERT INTO users (name, email, password, role) VALUES (?, ?, ?, ?)",
                          (name, email, password, role))
                conn.commit()
            return redirect(url_for('login'))
        except sqlite3.IntegrityError:
            return "Email already exists. Try logging in."

    return render_template('register.html')

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form['email']
        password = request.form['password']

        with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
            c = conn.cursor()
            c.execute("SELECT * FROM users WHERE email=? AND password=?", (email, password))
            user = c.fetchone()

        if user:
            session['user_id'] = user[0]
            session['role'] = user[4]
            return redirect(url_for('dashboard'))
        else:
            return "Invalid Credentials"

    return render_template('login.html')

# Dashboard
@app.route('/dashboard')
def dashboard():
    if 'user_id' not in session:
        return redirect(url_for('login'))

    with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
        c = conn.cursor()
        if session['role'] == 'recruiter':
            c.execute("SELECT * FROM jobs WHERE recruiter_id=?", (session['user_id'],))
            jobs = c.fetchall()
        else:
            # For job seekers, also fetch applications
            c.execute("SELECT * FROM jobs")
            jobs = c.fetchall()

            # Get list of job_ids the user already applied to
            c.execute("SELECT job_id FROM applications WHERE user_id=?", (session['user_id'],))
            applied_jobs = [row[0] for row in c.fetchall()]

    return render_template('dashboard.html', jobs=jobs, role=session['role'],
                           applied_jobs=applied_jobs if session['role'] == 'jobseeker' else [])

# Post Job (Recruiter)
@app.route('/post_job', methods=['GET', 'POST'])
def post_job():
    if 'user_id' not in session or session['role'] != 'recruiter':
        return redirect(url_for('login'))

    if request.method == 'POST':
        title = request.form['title']
        description = request.form['description']
        skills = request.form['skills']

        with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
            c = conn.cursor()
            c.execute("INSERT INTO jobs (title, description, skills, recruiter_id) VALUES (?, ?, ?, ?)",
                      (title, description, skills, session['user_id']))
            conn.commit()
        return redirect(url_for('dashboard'))

    return render_template('post_job.html')

# Apply Job (Job Seeker)
@app.route('/apply/<int:job_id>')
def apply(job_id):
    if 'user_id' not in session or session['role'] != 'jobseeker':
        return "You must log in as a Job Seeker to apply."

    with sqlite3.connect(DB_NAME, check_same_thread=False) as conn:
        c = conn.cursor()
        # Prevent duplicate applications
        c.execute("SELECT * FROM applications WHERE job_id=? AND user_id=?", (job_id, session['user_id']))
        if c.fetchone():
            return "You have already applied for this job."
        c.execute("INSERT INTO applications (job_id, user_id) VALUES (?, ?)", (job_id, session['user_id']))
        conn.commit()

    return redirect(url_for('dashboard'))

# Logout
@app.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# ---------------------------
# Run Flask App
# ---------------------------
if __name__ == '__main__':
    app.run(debug=True)
