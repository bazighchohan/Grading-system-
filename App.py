import streamlit as st
import pandas as pd

st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

st.title("🎓 GPA & CGPA Calculator")
st.write("Easily calculate your semester GPA and cumulative CGPA.")

# --- GPA Calculation Section ---
st.header("📌 Semester GPA Calculation")

num_courses = st.number_input("Number of Courses", min_value=1, max_value=20, value=5, step=1)

# DataFrame for input
data = []
for i in range(num_courses):
    col1, col2, col3 = st.columns([2, 1, 1])
    with col1:
        course = st.text_input(f"Course {i+1} Name", key=f"course_{i}")
    with col2:
        credit_hours = st.number_input(f"Credit Hours {i+1}", min_value=1.0, step=0.5, key=f"credit_{i}")
    with col3:
        grade_point = st.number_input(f"Grade Point {i+1} (0.0–4.0)", min_value=0.0, max_value=4.0, step=0.1, key=f"grade_{i}")
    data.append({"Course": course, "Credit Hours": credit_hours, "Grade Point": grade_point})

# Convert to DataFrame
df = pd.DataFrame(data)

# GPA Calculation
if not df.empty:
    total_credits = df["Credit Hours"].sum()
    total_points = (df["Credit Hours"] * df["Grade Point"]).sum()

    if total_credits > 0:
        gpa = total_points / total_credits
        st.success(f"🎯 **Your GPA for this semester is: {gpa:.2f}**")
    else:
        gpa = 0
        st.warning("Please enter valid credit hours.")
else:
    gpa = 0

# Show table
st.dataframe(df, use_container_width=True)

# --- CGPA Calculation Section ---
st.header("📌 CGPA Calculation")

prev_cgpa = st.number_input("Previous CGPA", min_value=0.0, max_value=4.0, step=0.01, value=0.0)
prev_credits = st.number_input("Total Credit Hours Completed Previously", min_value=0.0, step=0.5, value=0.0)

if st.button("Calculate CGPA"):
    total_credits_all = prev_credits + total_credits
    if total_credits_all > 0:
        new_cgpa = ((prev_cgpa * prev_credits) + (gpa * total_credits)) / total_credits_all
        st.success(f"📚 **Your updated CGPA is: {new_cgpa:.2f}**")
    else:
        st.warning("Enter valid previous credits or semester data.")
