# Hostel Management — Hostel Maintenance Priority System

A lightweight web application built with **Python** and **Streamlit** to streamline hostel maintenance complaint registration, priority classification, and real-time resolution tracking for students and hostel wardens.

---

## Key Features

- **Role-Based Access Control (Login Tab):**
  - **Student Login:** Direct access to submit new maintenance complaints and track complaint statuses.
  - **Warden Login:** Password-protected access (`warden123`) to view all complaints and update repair statuses.
- **Automated Priority Scoring (`calculate_priority`):**
  - Calculates priority dynamically using `score = urgency * severity` (both rated on a 1–5 scale).
  - Classifies issues into **HIGH** (`score >= 15`), **MEDIUM** (`score >= 8`), or **LOW** (`score < 8`).
- **Student Complaint Registration & Tracking (Student Tab):**
  - Captures Student Name, Block Number, Room Number, Problem Category (`Electrical`, `Plumbing`, `Furniture`, `Internet`, `Other`), Description, Urgency, and Severity.
  - Validates required fields (`Student Name` and `Room Number`) before saving.
  - Displays live complaint cards with color-coded status indicators (`Pending`, `In Progress`, `Resolved`).
- **Warden Management Dashboard (Warden Tab):**
  - Displays all submitted student complaints with full details and priority labels.
  - Allows wardens to update each complaint's status in real time via `st.session_state`.

---

## Tech Stack & Python Concepts Used

- **Language:** Python 3
- **Framework:** Streamlit (`st.tabs`, `st.selectbox`, `st.text_input`, `st.slider`, `st.session_state`)
- **Core Concepts:** User-defined functions (`calculate_priority`), conditional logic (`if-elif-else`), `for` loops, lists of dictionaries, and session state management.

---

## How to Run Locally

1. **Clone the repository:**
   git clone https://github.com/sumit-net/Hostel-Management_.git
   cd Hostel-Management_

2. **Install Streamlit:**
   pip install streamlit

3. **Run the application:**
   streamlit run app.py

---

## Team Members (Bennett University — 2026CSAE100)

- **Aditya Pandey** (Team Leader)
- **Sumit Verma** (`S26CSEU2563`)
- **Ritik Agarwal** (`S26CSEU2546`)
- **Anirudh Sharma** (`S26CSEU2454`)
- **Devansh Tiwari** (`S26CSEU2556`)
