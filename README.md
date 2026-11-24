Hostel Maintenance Priority System

A lightweight, role-based web application built with Python and Streamlit to streamline hostel maintenance complaint registration, priority classification, and real-time status tracking.

Overview

In university hostels, maintenance requests are often handled manually without evaluating urgency or severity. This application separates Student and Warden workflows using role-based tabs, automatically computes a priority level (HIGH, MEDIUM, or LOW) for every complaint, and allows wardens to update repair statuses in real time.

Key Features

Role-Based Login (Login Tab):

Student Access: Instant login without a password to log and track complaints.

Warden Access: Password-protected login (warden123) to manage and update all submitted complaints.

Automated Priority Calculation:

Computes a priority score using score = urgency * severity (both rated on a 1–5 scale):

HIGH: score >= 15

MEDIUM: score >= 8

LOW: score < 8

Student Complaint Portal (Student Tab):

Submit complaints across five categories: Electrical, Plumbing, Furniture, Internet, and Other.

Validates mandatory fields (Student Name and Room Number) before saving.

Displays live complaint cards with color-coded status alerts (Pending, In Progress, Resolved).

Warden Management Dashboard (Warden Tab):

Displays all active student complaints along with their computed priority levels.

Allows the warden to update any complaint's status (Pending, In Progress, Resolved) dynamically.

Tech Stack

Language: Python 3.x

Framework: Streamlit

State Management: streamlit.session_state (in-memory session persistence)

Installation & How to Run

Clone the repository:

git clone https://github.com/<your-username>/Hostel-Management_.git
cd Hostel-Management_


Install Streamlit:

pip install streamlit


Run the application:

streamlit run app.py


Open in browser:
Navigate to http://localhost:8501 if it does not open automatically.

Usage Guide

Login Tab:

Select Student and click Login to access the complaint form.

Select Warden, enter the default password (warden123), and click Login to access the admin dashboard.

Student Tab:

Fill in your Name, Block Number, Room Number, Category, Description, Urgency (1–5), and Severity (1–5), then click Submit Complaint.

Scroll down to My Complaints to monitor the live status of your submitted requests.

Warden Tab:

Review all complaints, choose a new status from the Update Status dropdown, and click Update.

Team Members (Bennett University — 2026CSAE100)

Aditya Pandey (Team Leader)

Sumit Verma (S26CSEU2563)

Ritik Agarwal (S26CSEU2546)

Anirudh Sharma (S26CSEU2454)

Devansh Tiwari (S26CSEU2556)

Future Improvements

Persist complaints to a CSV file or SQLite database so records remain saved across server restarts.

Sort complaints automatically from HIGH to LOW priority on the Warden dashboard.

Add unique Complaint IDs (CMP-XXXX) to prevent widget key collisions when the same student submits multiple complaints for the same room.
