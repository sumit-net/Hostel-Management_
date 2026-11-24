
import streamlit as st

# Calculate Priority
def calculate_priority(urgency, severity):
    score = urgency * severity

    if score >= 15:
        return "HIGH"
    elif score >= 8:
        return "MEDIUM"
    else:
        return "LOW"


# Store Complaints
if "complaints" not in st.session_state:
    st.session_state.complaints = []

if "role" not in st.session_state:
    st.session_state.role = ""


st.title("Hostel Maintenance Priority System")

tab1, tab2, tab3 = st.tabs(["Login", "Student", "Warden"])


# LOGIN
with tab1:
    st.header("Login")

    role = st.selectbox("Select Role", ["Student", "Warden"])
    password = st.text_input("Warden Password", type="password")

    if st.button("Login"):

        if role == "Student":
            st.session_state.role = "student"
            st.success("Student Login Successful")

        elif password == "warden123":
            st.session_state.role = "warden"
            st.success("Warden Login Successful")

        else:
            st.error("Wrong Password")


# STUDENT
with tab2:
    st.header("Register Complaint")

    if st.session_state.role != "student":
        st.warning("Please login as Student first.")

    else:
        name = st.text_input("Student Name")
        block = st.text_input("Block Number")
        room = st.text_input("Room Number")

        category = st.selectbox(
            "Problem Category",
            ["Electrical", "Plumbing", "Furniture", "Internet", "Other"]
        )

        description = st.text_area("Problem Description")

        urgency = st.slider("Urgency", 1, 5, 3)
        severity = st.slider("Severity", 1, 5, 3)

        if st.button("Submit Complaint"):

            if name == "" or room == "":
                st.error("Please fill Student Name and Room Number.")

            else:
                priority = calculate_priority(urgency, severity)

                complaint = {
                    "Name": name,
                    "Block": block,
                    "Room": room,
                    "Category": category,
                    "Description": description,
                    "Urgency": urgency,
                    "Severity": severity,
                    "Priority": priority,
                    "Status": "Pending"
                }

                st.session_state.complaints.append(complaint)

                st.success("Complaint Registered Successfully!")

        # Show Complaints
        st.divider()
        st.subheader("My Complaints")

        if len(st.session_state.complaints) == 0:
            st.info("No complaints available.")

        else:
            for complaint in st.session_state.complaints:

                st.write("----------------------")
                st.write("Student:", complaint["Name"])
                st.write("Block:", complaint["Block"])
                st.write("Room:", complaint["Room"])
                st.write("Category:", complaint["Category"])
                st.write("Description:", complaint["Description"])
                st.write("Urgency:", complaint["Urgency"])
                st.write("Severity:", complaint["Severity"])
                st.write("Priority:", complaint["Priority"])
                st.write("Current Status:", complaint["Status"])

                if complaint["Status"] == "Resolved":
                    st.success("Complaint Resolved!")

                elif complaint["Status"] == "In Progress":
                    st.info("Complaint is being processed.")

                else:
                    st.warning("Complaint is Pending.")


# WARDEN
with tab3:
    st.header("Warden Dashboard")

    if st.session_state.role != "warden":
        st.warning("Please login as Warden first.")

    else:
        if len(st.session_state.complaints) == 0:
            st.info("No complaints available.")

        else:
            for complaint in st.session_state.complaints:

                st.write("----------------------")
                st.write("Student:", complaint["Name"])
                st.write("Block:", complaint["Block"])
                st.write("Room:", complaint["Room"])
                st.write("Category:", complaint["Category"])
                st.write("Description:", complaint["Description"])
                st.write("Priority:", complaint["Priority"])
                st.write("Current Status:", complaint["Status"])

                new_status = st.selectbox(
                    "Update Status",
                    ["Pending", "In Progress", "Resolved"],
                    key=complaint["Name"] + complaint["Room"]
                )

                if st.button("Update"):
                  complaint["Status"] = new_status
                  st.success("Updated!")