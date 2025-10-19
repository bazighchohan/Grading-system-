# # import streamlit as st
# # import pandas as pd

# # st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

# # st.title("🎓 GPA & CGPA Calculator")
# # st.write("Easily calculate your semester GPA and cumulative CGPA.")

# # # --- GPA Calculation Section ---
# # st.header("📌 Semester GPA Calculation")

# # num_courses = st.number_input("Number of Courses", min_value=1, max_value=20, value=5, step=1)

# # # DataFrame for input
# # data = []
# # for i in range(num_courses):
# #     col1, col2, col3 = st.columns([2, 1, 1])
# #     with col1:
# #         course = st.text_input(f"Course {i+1} Name", key=f"course_{i}")
# #     with col2:
# #         credit_hours = st.number_input(f"Credit Hours {i+1}", min_value=1.0, step=0.5, key=f"credit_{i}")
# #     with col3:
# #         grade_point = st.number_input(f"Grade Point {i+1} (0.0–4.0)", min_value=0.0, max_value=4.0, step=0.1, key=f"grade_{i}")
# #     data.append({"Course": course, "Credit Hours": credit_hours, "Grade Point": grade_point})

# # # Convert to DataFrame
# # df = pd.DataFrame(data)

# # # GPA Calculation
# # if not df.empty:
# #     total_credits = df["Credit Hours"].sum()
# #     total_points = (df["Credit Hours"] * df["Grade Point"]).sum()

# #     if total_credits > 0:
# #         gpa = total_points / total_credits
# #         st.success(f"🎯 **Your GPA for this semester is: {gpa:.2f}**")
# #     else:
# #         gpa = 0
# #         st.warning("Please enter valid credit hours.")
# # else:
# #     gpa = 0

# # # Show table
# # st.dataframe(df, use_container_width=True)

# # # --- CGPA Calculation Section ---
# # st.header("📌 CGPA Calculation")

# # prev_cgpa = st.number_input("Previous CGPA", min_value=0.0, max_value=4.0, step=0.01, value=0.0)
# # prev_credits = st.number_input("Total Credit Hours Completed Previously", min_value=0.0, step=0.5, value=0.0)

# # if st.button("Calculate CGPA"):
# #     total_credits_all = prev_credits + total_credits
# #     if total_credits_all > 0:
# #         new_cgpa = ((prev_cgpa * prev_credits) + (gpa * total_credits)) / total_credits_all
# #         st.success(f"📚 **Your updated CGPA is: {new_cgpa:.2f}**")
# #     else:
# #         st.warning("Enter valid previous credits or semester data.")


# import streamlit as st
# import pandas as pd

# st.set_page_config(page_title="GPA & CGPA Calculator", page_icon="🎓", layout="centered")

# st.title("🎓 GPA & CGPA Calculator")
# st.write("This tool calculates your **GPA** and **CGPA** using total points method (your logic).")

# # -------------------- GPA CALCULATOR --------------------
# st.header("📌 Semester GPA Calculator")

# num_courses = st.number_input("Number of Courses", min_value=1, max_value=20, value=5, step=1)

# # For storing semester data
# semester_data = []
# for i in range(num_courses):
#     col1, col2, col3 = st.columns([2, 1, 1])
#     with col1:
#         course = st.text_input(f"Course {i+1} Name", key=f"course_{i}")
#     with col2:
#         credit_hours = st.number_input(f"Credit Hours {i+1}", min_value=1.0, step=0.5, key=f"credit_{i}")
#     with col3:
#         grade_point = st.number_input(f"Grade Point {i+1} (0.0–4.0)", min_value=0.0, max_value=4.0, step=0.1, key=f"grade_{i}")
#     semester_data.append({"Course": course, "Credit Hours": credit_hours, "Grade Point": grade_point})

# df = pd.DataFrame(semester_data)

# # GPA Calculation
# if not df.empty:
#     total_semester_credits = df["Credit Hours"].sum()
#     total_semester_points = (df["Credit Hours"] * df["Grade Point"]).sum()

#     if total_semester_credits > 0:
#         gpa = total_semester_points / total_semester_credits
#         st.success(f"🎯 **Your Semester GPA is: {gpa:.2f}**")
#     else:
#         gpa = 0
#         st.warning("Please enter valid credit hours.")
# else:
#     gpa = 0

# st.dataframe(df, use_container_width=True)

# # -------------------- CGPA CALCULATOR (Your Logic) --------------------
# st.header("📌 CGPA Calculator (Total Points Method)")

# st.write("""
# Enter your **total credit hours completed so far** and **total grade points earned**.  
# This uses the logic:  
# 👉 **Total Points Earned ÷ Total Credit Hours = CGPA**
# """)

# # Inputs for CGPA
# total_credits_completed = st.number_input("Total Credit Hours Completed", min_value=0.0, step=1.0, value=0.0)
# total_points_earned = st.number_input("Total Grade Points Earned (Sum of GPA×Credit Hours for all semesters)", min_value=0.0, step=0.1, value=0.0)

# # Optional: Add this semester to cumulative total
# if st.checkbox("Add this semester's GPA to cumulative automatically"):
#     total_credits_completed += total_semester_credits
#     total_points_earned += total_semester_points

# if total_credits_completed > 0:
#     cgpa = total_points_earned / total_credits_completed
#     st.success(f"📚 **Your CGPA is: {cgpa:.2f}**")
# else:
#     st.info("Enter your cumulative credit hours and points to calculate CGPA.")

# # -------------------- TARGET CGPA PLANNER --------------------
# st.header("🎯 Target CGPA Planner (Optional)")
# st.write("Plan how much GPA you need in remaining credit hours to reach a target CGPA.")

# target_cgpa = st.number_input("🎯 Target CGPA", min_value=0.0, max_value=4.0, step=0.01, value=3.5)
# remaining_credits = st.number_input("Remaining Credit Hours", min_value=0.0, step=1.0, value=0.0)

# if remaining_credits > 0:
#     required_future_gpa = ((target_cgpa * (total_credits_completed + remaining_credits)) - total_points_earned) / remaining_credits

#     if required_future_gpa > 4:
#         st.error(f"⚠️ Required future GPA is {required_future_gpa:.2f}, which is not achievable (over 4).")
#     else:
#         st.success(f"To reach CGPA {target_cgpa:.2f}, you need an average GPA of **{required_future_gpa:.2f}** in the remaining credits.")



import streamlit as st

st.set_page_config(layout="centered", page_title="CGPA Predictor")

st.title("Future CGPA Predictor 🔮")
st.write("Find out how your next semester will impact your overall CGPA.")


# --- Section 1: Current Standing ---
st.subheader("Your Current Standing")
st.write("Enter your totals *before* this new semester.")

col1, col2 = st.columns(2)

with col1:
    current_total_credits = st.number_input(
        "Current Total Credit Hours",
        min_value=1,
        value=120,
        help="How many credit hours have you completed so far?"
    )
    
with col2:
    current_cgpa = st.number_input(
        "Current CGPA",
        min_value=0.0,
        max_value=4.0, # Adjust if your scale is different
        step=0.01,
        value=3.50,
        help="Your cumulative GPA right now."
    )

# --- Section 2: New Semester ---
st.subheader("Your New Semester")
st.write("Enter your expected results for this semester.")

col3, col4 = st.columns(2)

with col3:
    new_semester_credits = st.number_input(
        "New Semester Credit Hours",
        min_value=1,
        value=15,
        help="How many credits are you taking?"
    )

with col4:
    new_semester_gpa = st.number_input(
        "New Semester Expected GPA",
        min_value=0.0,
        max_value=4.0, # Adjust if your scale is different
        step=0.01,
        value=3.80,
        help="What GPA do you expect to get this semester?"
    )

st.divider()

# --- Calculation ---
if st.button("Predict My New CGPA ✨"):

    # 1. Calculate old total points
    old_total_points = current_cgpa * current_total_credits
    
    # 2. Calculate new semester points
    new_semester_points = new_semester_gpa * new_semester_credits
    
    # 3. Calculate combined totals
    total_combined_points = old_total_points + new_semester_points
    total_combined_credits = current_total_credits + new_semester_credits
    
    # 4. Calculate new CGPA
    if total_combined_credits > 0:
        new_cgpa = total_combined_points / total_combined_credits
        
        st.header(f"Your New CGPA will be: {new_cgpa:.2f}")

        # Show a "before and after" comparison
        col5, col6 = st.columns(2)
        col5.metric(label="Old CGPA", value=f"{current_cgpa:.2f}")
        col6.metric(label="New CGPA", value=f"{new_cgpa:.2f}", delta=f"{new_cgpa - current_cgpa:.2f}")

        # Show the math in an expander
        with st.expander("See the calculation breakdown"):
            st.markdown(f"""
            - **Old Total Points:** {current_total_credits} credits × {current_cgpa} CGPA = `{old_total_points:.2f}` points
            - **New Semester Points:** {new_semester_credits} credits × {new_semester_gpa} GPA = `{new_semester_points:.2f}` points
            
            ---
            
            - **Total Combined Points:** `{old_total_points:.2f}` + `{new_semester_points:.2f}` = `{total_combined_points:.2f}`
            - **Total Combined Credits:** `{current_total_credits}` + `{new_semester_credits}` = `{total_combined_credits}`
            
            ---
            
            - **Final CGPA:** `{total_combined_points:.2f}` points / `{total_combined_credits}` credits = **`{new_cgpa:.2f}`**
            """)
    else:
        st.error("Please enter valid credit hours.")
