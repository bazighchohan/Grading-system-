

# # # # import streamlit as st

# # # # st.set_page_config(layout="centered", page_title="CGPA Predictor")

# # # # st.title("Future CGPA Predictor 🔮")
# # # # st.write("Find out how your next semester will impact your overall CGPA.")


# # # # # --- Section 1: Current Standing ---
# # # # st.subheader("Your Current Standing")
# # # # st.write("Enter your totals *before* this new semester.")

# # # # col1, col2 = st.columns(2)

# # # # with col1:
# # # #     current_total_credits = st.number_input(
# # # #         "Current Total Credit Hours",
# # # #         min_value=1,
# # # #         value=120,
# # # #         help="How many credit hours have you completed so far?"
# # # #     )
    
# # # # with col2:
# # # #     current_cgpa = st.number_input(
# # # #         "Current CGPA",
# # # #         min_value=0.0,
# # # #         max_value=4.0, # Adjust if your scale is different
# # # #         step=0.01,
# # # #         value=3.50,
# # # #         help="Your cumulative GPA right now."
# # # #     )

# # # # # --- Section 2: New Semester ---
# # # # st.subheader("Your New Semester")
# # # # st.write("Enter your expected results for this semester.")

# # # # col3, col4 = st.columns(2)

# # # # with col3:
# # # #     new_semester_credits = st.number_input(
# # # #         "New Semester Credit Hours",
# # # #         min_value=1,
# # # #         value=15,
# # # #         help="How many credits are you taking?"
# # # #     )

# # # # with col4:
# # # #     new_semester_gpa = st.number_input(
# # # #         "New Semester Expected GPA",
# # # #         min_value=0.0,
# # # #         max_value=4.0, # Adjust if your scale is different
# # # #         step=0.01,
# # # #         value=3.80,
# # # #         help="What GPA do you expect to get this semester?"
# # # #     )

# # # # st.divider()

# # # # # --- Calculation ---
# # # # if st.button("Predict My New CGPA ✨"):

# # # #     # 1. Calculate old total points
# # # #     old_total_points = current_cgpa * current_total_credits
    
# # # #     # 2. Calculate new semester points
# # # #     new_semester_points = new_semester_gpa * new_semester_credits
    
# # # #     # 3. Calculate combined totals
# # # #     total_combined_points = old_total_points + new_semester_points
# # # #     total_combined_credits = current_total_credits + new_semester_credits
    
# # # #     # 4. Calculate new CGPA
# # # #     if total_combined_credits > 0:
# # # #         new_cgpa = total_combined_points / total_combined_credits
        
# # # #         st.header(f"Your New CGPA will be: {new_cgpa:.2f}")

# # # #         # Show a "before and after" comparison
# # # #         col5, col6 = st.columns(2)
# # # #         col5.metric(label="Old CGPA", value=f"{current_cgpa:.2f}")
# # # #         col6.metric(label="New CGPA", value=f"{new_cgpa:.2f}", delta=f"{new_cgpa - current_cgpa:.2f}")

# # # #         # Show the math in an expander
# # # #         with st.expander("See the calculation breakdown"):
# # # #             st.markdown(f"""
# # # #             - **Old Total Points:** {current_total_credits} credits × {current_cgpa} CGPA = `{old_total_points:.2f}` points
# # # #             - **New Semester Points:** {new_semester_credits} credits × {new_semester_gpa} GPA = `{new_semester_points:.2f}` points
            
# # # #             ---
            
# # # #             - **Total Combined Points:** `{old_total_points:.2f}` + `{new_semester_points:.2f}` = `{total_combined_points:.2f}`
# # # #             - **Total Combined Credits:** `{current_total_credits}` + `{new_semester_credits}` = `{total_combined_credits}`
            
# # # #             ---
            
# # # #             - **Final CGPA:** `{total_combined_points:.2f}` points / `{total_combined_credits}` credits = **`{new_cgpa:.2f}`**
# # # #             """)
# # # #     else:
# # # #         st.error("Please enter valid credit hours.")

# # # import streamlit as st
# # # import pandas as pd

# # # st.set_page_config(layout="centered", page_title="GPA Toolkit")

# # # # -----------------------------------------------------------------------------
# # # # PAGE 1: GPA Calculator (Single Semester)
# # # # -----------------------------------------------------------------------------

# # # def gpa_calculator():
# # #     st.title("GPA Calculator")
# # #     st.write("Enter your courses, credits, and the numeric grade points for this semester.")

# # #     # --- Back to Home Button ---
# # #     if st.button("⬅️ Back to Home"):
# # #         st.session_state.page = "home"
# # #         st.rerun()  # Rerun the script to show the home page

# # #     num_courses = st.number_input("How many courses did you take?", min_value=1, value=4)
# # #     course_inputs = []

# # #     for i in range(num_courses):
# # #         st.write(f"--- Course {i+1} ---")
# # #         col1, col2 = st.columns(2)
        
# # #         with col1:
# # #             credits = st.number_input(
# # #                 f"Course {i+1} Credit Hours", 
# # #                 min_value=1, 
# # #                 max_value=6, 
# # #                 value=3, 
# # #                 key=f"credits_{i}"
# # #             )
# # #         with col2:
# # #             grade_point = st.number_input(
# # #                 f"Course {i+1} Grade Point",
# # #                 min_value=0.0,
# # #                 max_value=4.0, 
# # #                 step=0.1,
# # #                 value=3.0,
# # #                 key=f"grade_point_{i}"
# # #             )
# # #         course_inputs.append({'credits': credits, 'grade_point': grade_point})

# # #     if st.button("Calculate GPA"):
# # #         total_points = 0.0
# # #         total_credits = 0.0
# # #         courses_summary = []

# # #         for i, course in enumerate(course_inputs):
# # #             credits = course['credits']
# # #             grade_point = course['grade_point']
# # #             points = grade_point * credits
# # #             total_points += points
# # #             total_credits += credits
# # #             courses_summary.append({
# # #                 'Course': f"Course {i+1}", 
# # #                 'Credits': credits, 
# # #                 'Grade Point': grade_point
# # #             })

# # #         if total_credits > 0:
# # #             gpa = total_points / total_credits
# # #             st.success(f"**Your GPA is: {gpa:.2f}**")
# # #             st.write(f"Total Grade Points: {total_points:.2f}")
# # #             st.write(f"Total Credit Hours: {total_credits}")
# # #             st.subheader("Semester Summary")
# # #             df = pd.DataFrame(courses_summary, columns=['Course', 'Credits', 'Grade Point'])
# # #             st.dataframe(df)
# # #         else:
# # #             st.error("Please enter valid credit hours.")

# # # # -----------------------------------------------------------------------------
# # # # PAGE 2: CGPA Calculator (Multiple Semesters)
# # # # -----------------------------------------------------------------------------

# # # def cgpa_calculator():
# # #     st.title("CGPA Calculator")
# # #     st.write("Enter the GPA and total credit hours for each of your past semesters.")
    
# # #     # --- Back to Home Button ---
# # #     if st.button("⬅️ Back to Home"):
# # #         st.session_state.page = "home"
# # #         st.rerun()

# # #     num_semesters = st.number_input("How many semesters to include?", min_value=1, value=2)
# # #     semesters = []
# # #     total_weighted_points = 0.0
# # #     total_credits = 0.0

# # #     for i in range(num_semesters):
# # #         st.write(f"--- Semester {i+1} ---")
# # #         col1, col2 = st.columns(2)

# # #         with col1:
# # #             sem_gpa = st.number_input(
# # #                 f"Semester {i+1} GPA", 
# # #                 min_value=0.0, 
# # #                 max_value=4.0, 
# # #                 step=0.01, 
# # #                 value=3.5, 
# # #                 key=f"sem_gpa_{i}"
# # #             )
# # #         with col2:
# # #             sem_credits = st.number_input(
# # #                 f"Semester {i+1} Total Credit Hours", 
# # #                 min_value=1, 
# # #                 value=15, 
# # #                 key=f"sem_credits_{i}"
# # #             )
# # #         semesters.append({'Semester': f"Semester {i+1}", 'GPA': sem_gpa, 'Credits': sem_credits})
# # #         total_weighted_points += sem_gpa * sem_credits
# # #         total_credits += sem_credits

# # #     if st.button("Calculate CGPA"):
# # #         if total_credits > 0:
# # #             cgpa = total_weighted_points / total_credits
# # #             st.success(f"**Your CGPA is: {cgpa:.2f}**")
# # #             st.write(f"Total Weighted Points: {total_weighted_points:.2f}")
# # #             st.write(f"Total Credit Hours: {total_credits}")
# # #             st.subheader("Overall Summary")
# # #             df = pd.DataFrame(semesters)
# # #             st.dataframe(df)
# # #         else:
# # #             st.error("Please enter valid credit hours.")

# # # # -----------------------------------------------------------------------------
# # # # PAGE 3: Future CGPA Predictor
# # # # -----------------------------------------------------------------------------

# # # def cgpa_predictor():
# # #     st.title("Future CGPA Predictor 🔮")
# # #     st.write("Find out how your next semester will impact your overall CGPA.")

# # #     # --- Back to Home Button ---
# # #     if st.button("⬅️ Back to Home"):
# # #         st.session_state.page = "home"
# # #         st.rerun()

# # #     st.subheader("Your Current Standing")
# # #     col1, col2 = st.columns(2)
# # #     with col1:
# # #         current_total_credits = st.number_input(
# # #             "Current Total Credit Hours",
# # #             min_value=1,
# # #             value=120,
# # #         )
# # #     with col2:
# # #         current_cgpa = st.number_input(
# # #             "Current CGPA",
# # #             min_value=0.0,
# # #             max_value=4.0,
# # #             step=0.01,
# # #             value=3.50,
# # #         )

# # #     st.subheader("Your New Semester")
# # #     col3, col4 = st.columns(2)
# # #     with col3:
# # #         new_semester_credits = st.number_input(
# # #             "New Semester Credit Hours",
# # #             min_value=1,
# # #             value=15,
# # #         )
# # #     with col4:
# # #         new_semester_gpa = st.number_input(
# # #             "New Semester Expected GPA",
# # #             min_value=0.0,
# # #             max_value=4.0,
# # #             step=0.01,
# # #             value=3.80,
# # #         )

# # #     st.divider()

# # #     if st.button("Predict My New CGPA ✨"):
# # #         old_total_points = current_cgpa * current_total_credits
# # #         new_semester_points = new_semester_gpa * new_semester_credits
# # #         total_combined_points = old_total_points + new_semester_points
# # #         total_combined_credits = current_total_credits + new_semester_credits
        
# # #         if total_combined_credits > 0:
# # #             new_cgpa = total_combined_points / total_combined_credits
# # #             st.header(f"Your New CGPA will be: {new_cgpa:.2f}")
# # #             col5, col6 = st.columns(2)
# # #             col5.metric(label="Old CGPA", value=f"{current_cgpa:.2f}")
# # #             col6.metric(label="New CGPA", value=f"{new_cgpa:.2f}", delta=f"{new_cgpa - current_cgpa:.2f}")
            
# # #             with st.expander("See the calculation breakdown"):
# # #                 st.markdown(f"""
# # #                 - **Old Total Points:** `{current_total_credits}` credits × `{current_cgpa}` CGPA = `{old_total_points:.2f}`
# # #                 - **New Semester Points:** `{new_semester_credits}` credits × `{new_semester_gpa}` GPA = `{new_semester_points:.2f}`
# # #                 - **Total Combined Points:** `{total_combined_points:.2f}`
# # #                 - **Total Combined Credits:** `{total_combined_credits}`
# # #                 - **Final CGPA:** `{total_combined_points:.2f}` / `{total_combined_credits}` = **`{new_cgpa:.2f}`**
# # #                 """)
# # #         else:
# # #             st.error("Please enter valid credit hours.")

# # # # -----------------------------------------------------------------------------
# # # # PAGE 0: Home / Navigation Page
# # # # -----------------------------------------------------------------------------

# # # def home_page():
# # #     st.title("Welcome to the GPA Toolkit")
# # #     st.subheader("Choose a calculator to get started:")

# # #     # Create 3 columns to center the buttons. 
# # #     # The first and last are spacers.
# # #     col1, col2, col3 = st.columns([1, 2, 1])

# # #     with col2:
# # #         # We use st.container() with a border to make the "squares"
# # #         # and st.button() to make them clickable.
        
# # #         with st.container(border=True):
# # #             st.subheader("GPA Calculator")
# # #             st.write("Calculate your GPA for a single semester.")
# # #             if st.button("Go to GPA", key="gpa_nav", use_container_width=True):
# # #                 st.session_state.page = "gpa"
# # #                 st.rerun()

# # #         with st.container(border=True):
# # #             st.subheader("CGPA Calculator")
# # #             st.write("Calculate your CGPA from all past semesters.")
# # #             if st.button("Go to CGPA", key="cgpa_nav", use_container_width=True):
# # #                 st.session_state.page = "cgpa"
# # #                 st.rerun()
        
# # #         with st.container(border=True):
# # #             st.subheader("Future CGPA Predictor")
# # #             st.write("See how your next semester will affect your CGPA.")
# # #             if st.button("Go to Predictor", key="predict_nav", use_container_width=True):
# # #                 st.session_state.page = "predict"
# # #                 st.rerun()


# # # # -----------------------------------------------------------------------------
# # # # Main App Logic: This part controls which page is shown
# # # # -----------------------------------------------------------------------------

# # # # Initialize session_state if it's not already set
# # # if "page" not in st.session_state:
# # #     st.session_state.page = "home"

# # # # Page router
# # # if st.session_state.page == "home":
# # #     home_page()
# # # elif st.session_state.page == "gpa":
# # #     gpa_calculator()
# # # elif st.session_state.page == "cgpa":
# # #     cgpa_calculator()
# # # elif st.session_state.page == "predict":
# # #     cgpa_predictor()
# # import streamlit as st
# # import pandas as pd

# # st.set_page_config(layout="wide", page_title="GPA Toolkit") # Changed layout to "wide" for a better horizontal fit

# # # -----------------------------------------------------------------------------
# # # PAGE 1: GPA Calculator (Single Semester)
# # # -----------------------------------------------------------------------------

# # def gpa_calculator():
# #     st.title("GPA Calculator")
# #     st.write("Enter your courses, credits, and the numeric grade points for this semester.")

# #     # --- Back to Home Button ---
# #     if st.button("⬅️ Back to Home"):
# #         st.session_state.page = "home"
# #         st.rerun()  # Rerun the script to show the home page

# #     num_courses = st.number_input("How many courses did you take?", min_value=1, value=4)
# #     course_inputs = []

# #     for i in range(num_courses):
# #         st.write(f"--- Course {i+1} ---")
# #         col1, col2 = st.columns(2)
        
# #         with col1:
# #             credits = st.number_input(
# #                 f"Course {i+1} Credit Hours", 
# #                 min_value=1, 
# #                 max_value=6, 
# #                 value=3, 
# #                 key=f"credits_{i}"
# #             )
# #         with col2:
# #             grade_point = st.number_input(
# #                 f"Course {i+1} Grade Point",
# #                 min_value=0.0,
# #                 max_value=4.0, 
# #                 step=0.1,
# #                 value=3.0,
# #                 key=f"grade_point_{i}"
# #             )
# #         course_inputs.append({'credits': credits, 'grade_point': grade_point})

# #     if st.button("Calculate GPA"):
# #         total_points = 0.0
# #         total_credits = 0.0
# #         courses_summary = []

# #         for i, course in enumerate(course_inputs):
# #             credits = course['credits']
# #             grade_point = course['grade_point']
# #             points = grade_point * credits
# #             total_points += points
# #             total_credits += credits
# #             courses_summary.append({
# #                 'Course': f"Course {i+1}", 
# #                 'Credits': credits, 
# #                 'Grade Point': grade_point
# #             })

# #         if total_credits > 0:
# #             gpa = total_points / total_credits
# #             st.success(f"**Your GPA is: {gpa:.2f}**")
# #             st.write(f"Total Grade Points: {total_points:.2f}")
# #             st.write(f"Total Credit Hours: {total_credits}")
# #             st.subheader("Semester Summary")
# #             df = pd.DataFrame(courses_summary, columns=['Course', 'Credits', 'Grade Point'])
# #             st.dataframe(df)
# #         else:
# #             st.error("Please enter valid credit hours.")

# # # -----------------------------------------------------------------------------
# # # PAGE 2: CGPA Calculator (Multiple Semesters)
# # # -----------------------------------------------------------------------------

# # def cgpa_calculator():
# #     st.title("CGPA Calculator")
# #     st.write("Enter the GPA and total credit hours for each of your past semesters.")
    
# #     # --- Back to Home Button ---
# #     if st.button("⬅️ Back to Home"):
# #         st.session_state.page = "home"
# #         st.rerun()

# #     num_semesters = st.number_input("How many semesters to include?", min_value=1, value=2)
# #     semesters = []
# #     total_weighted_points = 0.0
# #     total_credits = 0.0

# #     for i in range(num_semesters):
# #         st.write(f"--- Semester {i+1} ---")
# #         col1, col2 = st.columns(2)

# #         with col1:
# #             sem_gpa = st.number_input(
# #                 f"Semester {i+1} GPA", 
# #                 min_value=0.0, 
# #                 max_value=4.0, 
# #                 step=0.01, 
# #                 value=3.5, 
# #                 key=f"sem_gpa_{i}"
# #             )
# #         with col2:
# #             sem_credits = st.number_input(
# #                 f"Semester {i+1} Total Credit Hours", 
# #                 min_value=1, 
# #                 value=15, 
# #                 key=f"sem_credits_{i}"
# #             )
# #         semesters.append({'Semester': f"Semester {i+1}", 'GPA': sem_gpa, 'Credits': sem_credits})
# #         total_weighted_points += sem_gpa * sem_credits
# #         total_credits += sem_credits

# #     if st.button("Calculate CGPA"):
# #         if total_credits > 0:
# #             cgpa = total_weighted_points / total_credits
# #             st.success(f"**Your CGPA is: {cgpa:.2f}**")
# #             st.write(f"Total Weighted Points: {total_weighted_points:.2f}")
# #             st.write(f"Total Credit Hours: {total_credits}")
# #             st.subheader("Overall Summary")
# #             df = pd.DataFrame(semesters)
# #             st.dataframe(df)
# #         else:
# #             st.error("Please enter valid credit hours.")

# # # -----------------------------------------------------------------------------
# # # PAGE 3: Future CGPA Predictor
# # # -----------------------------------------------------------------------------

# # def cgpa_predictor():
# #     st.title("Future CGPA Predictor 🔮")
# #     st.write("Find out how your next semester will impact your overall CGPA.")

# #     # --- Back to Home Button ---
# #     if st.button("⬅️ Back to Home"):
# #         st.session_state.page = "home"
# #         st.rerun()

# #     st.subheader("Your Current Standing")
# #     col1, col2 = st.columns(2)
# #     with col1:
# #         current_total_credits = st.number_input(
# #             "Current Total Credit Hours",
# #             min_value=1,
# #             value=120,
# #         )
# #     with col2:
# #         current_cgpa = st.number_input(
# #             "Current CGPA",
# #             min_value=0.0,
# #             max_value=4.0,
# #             step=0.01,
# #             value=3.50,
# #         )

# #     st.subheader("Your New Semester")
# #     col3, col4 = st.columns(2)
# #     with col3:
# #         new_semester_credits = st.number_input(
# #             "New Semester Credit Hours",
# #             min_value=1,
# #             value=15,
# #         )
# #     with col4:
# #         new_semester_gpa = st.number_input(
# #             "New Semester Expected GPA",
# #             min_value=0.0,
# #             max_value=4.0,
# #             step=0.01,
# #             value=3.80,
# #         )

# #     st.divider()

# #     if st.button("Predict My New CGPA ✨"):
# #         old_total_points = current_cgpa * current_total_credits
# #         new_semester_points = new_semester_gpa * new_semester_credits
# #         total_combined_points = old_total_points + new_semester_points
# #         total_combined_credits = current_total_credits + new_semester_credits
        
# #         if total_combined_credits > 0:
# #             new_cgpa = total_combined_points / total_combined_credits
# #             st.header(f"Your New CGPA will be: {new_cgpa:.2f}")
# #             col5, col6 = st.columns(2)
# #             col5.metric(label="Old CGPA", value=f"{current_cgpa:.2f}")
# #             col6.metric(label="New CGPA", value=f"{new_cgpa:.2f}", delta=f"{new_cgpa - current_cgpa:.2f}")
            
# #             with st.expander("See the calculation breakdown"):
# #                 st.markdown(f"""
# #                 - **Old Total Points:** `{current_total_credits}` credits × `{current_cgpa}` CGPA = `{old_total_points:.2f}`
# #                 - **New Semester Points:** `{new_semester_credits}` credits × `{new_semester_gpa}` GPA = `{new_semester_points:.2f}`
# #                 - **Total Combined Points:** `{total_combined_points:.2f}`
# #                 - **Total Combined Credits:** `{total_combined_credits}`
# #                 - **Final CGPA:** `{total_combined_points:.2f}` / `{total_combined_credits}` = **`{new_cgpa:.2f}`**
# #                 """)
# #         else:
# #             st.error("Please enter valid credit hours.")

# # # -----------------------------------------------------------------------------
# # # PAGE 0: Home / Navigation Page (*** THIS IS THE UPDATED PART ***)
# # # -----------------------------------------------------------------------------

# # def home_page():
# #     st.title("Welcome to the GPA Toolkit")
# #     st.subheader("Choose a calculator to get started:")

# #     # Create 3 equal columns for a horizontal layout
# #     col1, col2, col3 = st.columns(3, gap="large")

# #     # Column 1: GPA Calculator
# #     with col1:
# #         with st.container(border=True):
# #             st.subheader("GPA Calculator")
# #             st.write("Calculate your GPA for a single semester.")
# #             if st.button("Go to GPA", key="gpa_nav", use_container_width=True):
# #                 st.session_state.page = "gpa"
# #                 st.rerun()

# #     # Column 2: CGPA Calculator
# #     with col2:
# #         with st.container(border=True):
# #             st.subheader("CGPA Calculator")
# #             st.write("Calculate your CGPA from all past semesters.")
# #             if st.button("Go to CGPA", key="cgpa_nav", use_container_width=True):
# #                 st.session_state.page = "cgpa"
# #                 st.rerun()
    
# #     # Column 3: Future CGPA Predictor
# #     with col3:
# #         with st.container(border=True):
# #             st.subheader("Future CGPA Predictor")
# #             st.write("See how your next semester will affect your CGPA.")
# #             if st.button("Go to Predictor", key="predict_nav", use_container_width=True):
# #                 st.session_state.page = "predict"
# #                 st.rerun()


# # # -----------------------------------------------------------------------------
# # # Main App Logic: This part controls which page is shown
# # # -----------------------------------------------------------------------------

# # # Initialize session_state if it's not already set
# # if "page" not in st.session_state:
# #     st.session_state.page = "home"

# # # Page router
# # if st.session_state.page == "home":
# #     home_page()
# # elif st.session_state.page == "gpa":
# #     gpa_calculator()
# # elif st.session_state.page == "cgpa":
# #     cgpa_calculator()
# # elif st.session_state.page == "predict":
# #     cgpa_predictor()


# import streamlit as st
# import pandas as pd

# # Use wide layout for the home page, but "centered" for the calculators
# # We will set this on a per-page basis
# # st.set_page_config(layout="wide", page_title="GPA Toolkit")

# # -----------------------------------------------------------------------------
# # PAGE 1: GPA Calculator (Single Semester) - (*** THIS IS THE UPDATED PART ***)
# # -----------------------------------------------------------------------------

# def gpa_calculator():
#     st.set_page_config(layout="centered", page_title="GPA Calculator") # Keep this page centered
    
#     st.title("GPA Calculator")
#     st.write("Enter your courses, credits, and the numeric grade points for this semester.")

#     # --- Back to Home Button ---
#     if st.button("⬅️ Back to Home"):
#         st.session_state.page = "home"
#         st.rerun()  # Rerun the script to show the home page

#     num_courses = st.number_input("How many courses did you take?", min_value=1, value=4)
#     course_inputs = []

#     for i in range(num_courses):
#         st.write(f"--- Entry {i+1} ---")
        
#         # *** CHANGED: Use 3 columns ***
#         col1, col2, col3 = st.columns(3)
        
#         with col1:
#             # *** NEW: Added Course Name input ***
#             course_name = st.text_input(
#                 "Course Name", 
#                 placeholder=f"e.g., Course {i+1}", 
#                 key=f"name_{i}"
#             )
        
#         with col2:
#             credits = st.number_input(
#                 "Credit Hours", 
#                 min_value=1, 
#                 max_value=6, 
#                 value=3, 
#                 key=f"credits_{i}"
#             )
            
#         with col3:
#             grade_point = st.number_input(
#                 "Grade Point",
#                 min_value=0.0,
#                 max_value=4.0, 
#                 step=0.1,
#                 value=3.0,
#                 key=f"grade_point_{i}"
#             )
            
#         # Add all three inputs to the list
#         course_inputs.append({
#             'name': course_name, 
#             'credits': credits, 
#             'grade_point': grade_point
#         })

#     if st.button("Calculate GPA"):
#         total_points = 0.0
#         total_credits = 0.0
#         courses_summary = []

#         for i, course in enumerate(course_inputs):
#             credits = course['credits']
#             grade_point = course['grade_point']
            
#             # Use the entered name, or a default if blank
#             name = course['name'] if course['name'] else f"Course {i+1}"
            
#             points = grade_point * credits
#             total_points += points
#             total_credits += credits
            
#             # *** CHANGED: Add the proper name to the summary ***
#             courses_summary.append({
#                 'Course': name, 
#                 'Credits': credits, 
#                 'Grade Point': grade_point
#             })

#         if total_credits > 0:
#             gpa = total_points / total_credits
#             st.success(f"**Your GPA is: {gpa:.2f}**")
#             st.write(f"Total Grade Points: {total_points:.2f}")
#             st.write(f"Total Credit Hours: {total_credits}")
#             st.subheader("Semester Summary")
            
#             # The dataframe headers are already correct
#             df = pd.DataFrame(courses_summary, columns=['Course', 'Credits', 'Grade Point'])
#             st.dataframe(df)
#         else:
#             st.error("Please enter valid credit hours.")

# # -----------------------------------------------------------------------------
# # PAGE 2: CGPA Calculator (Multiple Semesters) - (No changes)
# # -----------------------------------------------------------------------------

# def cgpa_calculator():
#     st.set_page_config(layout="centered", page_title="CGPA Calculator") # Keep this page centered
    
#     st.title("CGPA Calculator")
#     st.write("Enter the GPA and total credit hours for each of your past semesters.")
    
#     if st.button("⬅️ Back to Home"):
#         st.session_state.page = "home"
#         st.rerun()

#     num_semesters = st.number_input("How many semesters to include?", min_value=1, value=2)
#     semesters = []
#     total_weighted_points = 0.0
#     total_credits = 0.0

#     for i in range(num_semesters):
#         st.write(f"--- Semester {i+1} ---")
#         col1, col2 = st.columns(2)

#         with col1:
#             sem_gpa = st.number_input(
#                 f"Semester {i+1} GPA", 
#                 min_value=0.0, 
#                 max_value=4.0, 
#                 step=0.01, 
#                 value=3.5, 
#                 key=f"sem_gpa_{i}"
#             )
#         with col2:
#             sem_credits = st.number_input(
#                 f"Semester {i+1} Total Credit Hours", 
#                 min_value=1, 
#                 value=15, 
#                 key=f"sem_credits_{i}"
#             )
#         semesters.append({'Semester': f"Semester {i+1}", 'GPA': sem_gpa, 'Credits': sem_credits})
#         total_weighted_points += sem_gpa * sem_credits
#         total_credits += sem_credits

#     if st.button("Calculate CGPA"):
#         if total_credits > 0:
#             cgpa = total_weighted_points / total_credits
#             st.success(f"**Your CGPA is: {cgpa:.2f}**")
#             st.write(f"Total Weighted Points: {total_weighted_points:.2f}")
#             st.write(f"Total Credit Hours: {total_credits}")
#             st.subheader("Overall Summary")
#             df = pd.DataFrame(semesters)
#             st.dataframe(df)
#         else:
#             st.error("Please enter valid credit hours.")

# # -----------------------------------------------------------------------------
# # PAGE 3: Future CGPA Predictor - (No changes)
# # -----------------------------------------------------------------------------

# def cgpa_predictor():
#     st.set_page_config(layout="centered", page_title="CGPA Predictor") # Keep this page centered
    
#     st.title("Future CGPA Predictor 🔮")
#     st.write("Find out how your next semester will impact your overall CGPA.")

#     if st.button("⬅️ Back to Home"):
#         st.session_state.page = "home"
#         st.rerun()

#     st.subheader("Your Current Standing")
#     col1, col2 = st.columns(2)
#     with col1:
#         current_total_credits = st.number_input(
#             "Current Total Credit Hours",
#             min_value=1,
#             value=120,
#         )
#     with col2:
#         current_cgpa = st.number_input(
#             "Current CGPA",
#             min_value=0.0,
#             max_value=4.0,
#             step=0.01,
#             value=3.50,
#         )

#     st.subheader("Your New Semester")
#     col3, col4 = st.columns(2)
#     with col3:
#         new_semester_credits = st.number_input(
#             "New Semester Credit Hours",
#             min_value=1,
#             value=15,
#         )
#     with col4:
#         new_semester_gpa = st.number_input(
#             "New Semester Expected GPA",
#             min_value=0.0,
#             max_value=4.0,
#             step=0.01,
#             value=3.80,
#         )

#     st.divider()

#     if st.button("Predict My New CGPA ✨"):
#         old_total_points = current_cgpa * current_total_credits
#         new_semester_points = new_semester_gpa * new_semester_credits
#         total_combined_points = old_total_points + new_semester_points
#         total_combined_credits = current_total_credits + new_semester_credits
        
#         if total_combined_credits > 0:
#             new_cgpa = total_combined_points / total_combined_credits
#             st.header(f"Your New CGPA will be: {new_cgpa:.2f}")
#             col5, col6 = st.columns(2)
#             col5.metric(label="Old CGPA", value=f"{current_cgpa:.2f}")
#             col6.metric(label="New CGPA", value=f"{new_cgpa:.2f}", delta=f"{new_cgpa - current_cgpa:.2f}")
            
#             with st.expander("See the calculation breakdown"):
#                 st.markdown(f"""
#                 - **Old Total Points:** `{current_total_credits}` credits × `{current_cgpa}` CGPA = `{old_total_points:.2f}`
#                 - **New Semester Points:** `{new_semester_credits}` credits × `{new_semester_gpa}` GPA = `{new_semester_points:.2f}`
#                 - **Total Combined Points:** `{total_combined_points:.2f}`
#                 - **Total Combined Credits:** `{total_combined_credits}`
#                 - **Final CGPA:** `{total_combined_points:.2f}` / `{total_combined_credits}` = **`{new_cgpa:.2f}`**
#                 """)
#         else:
#             st.error("Please enter valid credit hours.")

# # -----------------------------------------------------------------------------
# # PAGE 0: Home / Navigation Page - (No changes)
# # -----------------------------------------------------------------------------

# def home_page():
#     st.set_page_config(layout="wide", page_title="GPA Toolkit") # Use "wide" for the home page
    
#     st.title("Welcome to the GPA Toolkit")
#     st.subheader("Choose a calculator to get started:")

#     # Create 3 equal columns for a horizontal layout
#     col1, col2, col3 = st.columns(3, gap="large")

#     # Column 1: GPA Calculator
#     with col1:
#         with st.container(border=True):
#             st.subheader("GPA Calculator")
#             st.write("Calculate your GPA for a single semester.")
#             if st.button("Go to GPA", key="gpa_nav", use_container_width=True):
#                 st.session_state.page = "gpa"
#                 st.rerun()

#     # Column 2: CGPA Calculator
#     with col2:
#         with st.container(border=True):
#             st.subheader("CGPA Calculator")
#             st.write("Calculate your CGPA from all past semesters.")
#             if st.button("Go to CGPA", key="cgpa_nav", use_container_width=True):
#                 st.session_state.page = "cgpa"
#                 st.rerun()
    
#     # Column 3: Future CGPA Predictor
#     with col3:
#         with st.container(border=True):
#             st.subheader("Future CGPA Predictor")
#             st.write("See how your next semester will affect your CGPA.")
#             if st.button("Go to Predictor", key="predict_nav", use_container_width=True):
#                 st.session_state.page = "predict"
#                 st.rerun()


# # -----------------------------------------------------------------------------
# # Main App Logic: This part controls which page is shown
# # -----------------------------------------------------------------------------

# if "page" not in st.session_state:
#     st.session_state.page = "home"

# if st.session_state.page == "home":
#     home_page()
# elif st.session_state.page == "gpa":
#     gpa_calculator()
# elif st.session_state.page == "cgpa":
#     cgpa_calculator()
# elif st.session_state.page == "predict":
#     cgpa_predictor()
import streamlit as st
import pandas as pd

# -----------------------------------------------------------------------------
# PAGE 1: GPA Calculator (Single Semester) - (No changes)
# -----------------------------------------------------------------------------

def gpa_calculator():
    st.set_page_config(layout="centered", page_title="GPA Calculator") 
    
    st.title("GPA Calculator")
    st.write("Enter your courses, credits, and the numeric grade points for this semester.")

    # --- Back to Home Button ---
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()  

    num_courses = st.number_input("How many courses did you take?", min_value=1, value=4)
    course_inputs = []

    for i in range(num_courses):
        st.write(f"--- Entry {i+1} ---")
        col1, col2, col3 = st.columns(3)
        
        with col1:
            course_name = st.text_input(
                "Course Name", 
                placeholder=f"e.g., Course {i+1}", 
                key=f"name_{i}"
            )
        with col2:
            credits = st.number_input(
                "Credit Hours", 
                min_value=1, 
                max_value=6, 
                value=3, 
                key=f"credits_{i}"
            )
        with col3:
            grade_point = st.number_input(
                "Grade Point",
                min_value=0.0,
                max_value=4.0, 
                step=0.1,
                value=3.0,
                key=f"grade_point_{i}"
            )
            
        course_inputs.append({
            'name': course_name, 
            'credits': credits, 
            'grade_point': grade_point
        })

    if st.button("Calculate GPA"):
        total_points = 0.0
        total_credits = 0.0
        courses_summary = []

        for i, course in enumerate(course_inputs):
            credits = course['credits']
            grade_point = course['grade_point']
            name = course['name'] if course['name'] else f"Course {i+1}"
            points = grade_point * credits
            total_points += points
            total_credits += credits
            courses_summary.append({
                'Course': name, 
                'Credits': credits, 
                'Grade Point': grade_point
            })

        if total_credits > 0:
            gpa = total_points / total_credits
            st.success(f"**Your GPA is: {gpa:.2f}**")
            st.write(f"Total Grade Points: {total_points:.2f}")
            st.write(f"Total Credit Hours: {total_credits}")
            st.subheader("Semester Summary")
            df = pd.DataFrame(courses_summary, columns=['Course', 'Credits', 'Grade Point'])
            st.dataframe(df)
        else:
            st.error("Please enter valid credit hours.")

# -----------------------------------------------------------------------------
# PAGE 2: Semester Analyzer (*** THIS IS THE NEW CODE ***)
# -----------------------------------------------------------------------------

def semester_analyzer():
    st.set_page_config(layout="centered", page_title="Semester Analyzer")
    
    st.title("Semester Analyzer 📈")
    st.write("Enter your credits and CGPA *after* each semester to find your individual semester GPA.")
    st.info("This is useful when your portal only shows your new CGPA, not your semester GPA.")
    
    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    num_semesters = st.number_input("How many semesters to analyze?", min_value=1, value=2)
    
    semester_inputs = []

    for i in range(num_semesters):
        st.write(f"--- Semester {i+1} ---")
        col1, col2 = st.columns(2)

        with col1:
            sem_credits = st.number_input(
                f"Credits in Semester {i+1}", 
                min_value=1, 
                value=15, 
                key=f"sem_credits_{i}"
            )
        with col2:
            sem_cgpa = st.number_input(
                f"CGPA *after* Semester {i+1}", 
                min_value=0.0, 
                max_value=4.0, 
                step=0.01, 
                value=3.20, 
                key=f"sem_cgpa_{i}"
            )
            
        semester_inputs.append({
            'sem_credits': sem_credits,
            'sem_cgpa': sem_cgpa
        })

    if st.button("Analyze Semesters"):
        results = []
        previous_total_points = 0.0
        previous_total_credits = 0.0
        
        all_valid = True
        
        for i, semester in enumerate(semester_inputs):
            sem_credits = semester['sem_credits']
            sem_cgpa = semester['sem_cgpa']
            
            # Calculate new totals based on user input
            current_total_credits = previous_total_credits + sem_credits
            current_total_points = current_total_credits * sem_cgpa
            
            # Isolate this semester's points
            semester_points = current_total_points - previous_total_points
            
            # Calculate this semester's GPA
            semester_gpa = 0.0
            if sem_credits > 0:
                semester_gpa = semester_points / sem_credits
            
            # Check for logical errors (e.g., negative GPA, which means CGPA went down too much)
            if semester_gpa < 0 or semester_gpa > 4.01: # (allow for small rounding errors)
                st.error(f"Error in Semester {i+1}: The CGPA you entered ({sem_cgpa}) is not possible with the credits from the previous semester. Please check your numbers.", icon="🚨")
                all_valid = False
                break
                
            results.append({
                'Semester': f"Semester {i+1}",
                'Semester Credits': sem_credits,
                'Semester GPA': f"{semester_gpa:.2f}",
                'Cumulative CGPA': f"{sem_cgpa:.2f}"
            })
            
            # Update trackers for the next loop
            previous_total_points = current_total_points
            previous_total_credits = current_total_credits

        if all_valid:
            st.subheader("Semester Analysis Results")
            df = pd.DataFrame(results)
            st.dataframe(df)


# -----------------------------------------------------------------------------
# PAGE 3: Future CGPA Predictor - (No changes)
# -----------------------------------------------------------------------------

def cgpa_predictor():
    st.set_page_config(layout="centered", page_title="CGPA Predictor")
    
    st.title("Future CGPA Predictor 🔮")
    st.write("Find out how your next semester will impact your overall CGPA.")

    if st.button("⬅️ Back to Home"):
        st.session_state.page = "home"
        st.rerun()

    st.subheader("Your Current Standing")
    col1, col2 = st.columns(2)
    with col1:
        current_total_credits = st.number_input(
            "Current Total Credit Hours",
            min_value=1,
            value=120,
        )
    with col2:
        current_cgpa = st.number_input(
            "Current CGPA",
            min_value=0.0,
            max_value=4.0,
            step=0.01,
            value=3.50,
        )

    st.subheader("Your New Semester")
    col3, col4 = st.columns(2)
    with col3:
        new_semester_credits = st.number_input(
            "New Semester Credit Hours",
            min_value=1,
            value=15,
        )
    with col4:
        new_semester_gpa = st.number_input(
            "New Semester Expected GPA",
            min_value=0.0,
            max_value=4.0,
            step=0.01,
            value=3.80,
        )

    st.divider()

    if st.button("Predict My New CGPA ✨"):
        old_total_points = current_cgpa * current_total_credits
        new_semester_points = new_semester_gpa * new_semester_credits
        total_combined_points = old_total_points + new_semester_points
        total_combined_credits = current_total_credits + new_semester_credits
        
        if total_combined_credits > 0:
            new_cgpa = total_combined_points / total_combined_credits
            st.header(f"Your New CGPA will be: {new_cgpa:.2f}")
            col5, col6 = st.columns(2)
            col5.metric(label="Old CGPA", value=f"{current_cgpa:.2f}")
            col6.metric(label="New CGPA", value=f"{new_cgpa:.2f}", delta=f"{new_cgpa - current_cgpa:.2f}")
            
            with st.expander("See the calculation breakdown"):
                st.markdown(f"""
                - **Old Total Points:** `{current_total_credits}` credits × `{current_cgpa}` CGPA = `{old_total_points:.2f}`
                - **New Semester Points:** `{new_semester_credits}` credits × `{new_semester_gpa}` GPA = `{new_semester_points:.2f}`
                - **Total Combined Points:** `{total_combined_points:.2f}`
                - **Total Combined Credits:** `{total_combined_credits}`
                - **Final CGPA:** `{total_combined_points:.2f}` / `{total_combined_credits}` = **`{new_cgpa:.2f}`**
                """)
        else:
            st.error("Please enter valid credit hours.")

# -----------------------------------------------------------------------------
# PAGE 0: Home / Navigation Page (*** UPDATED THIS SECTION ***)
# -----------------------------------------------------------------------------

def home_page():
    st.set_page_config(layout="wide", page_title="GPA Toolkit") 
    
    st.title("Welcome to the GPA Toolkit")
    st.subheader("Choose a calculator to get started:")

    col1, col2, col3 = st.columns(3, gap="large")

    # Column 1: GPA Calculator
    with col1:
        with st.container(border=True):
            st.subheader("GPA Calculator")
            st.write("Calculate your GPA for a single semester.")
            if st.button("Go to GPA", key="gpa_nav", use_container_width=True):
                st.session_state.page = "gpa"
                st.rerun()

    # Column 2: Semester Analyzer (*** UPDATED ***)
    with col2:
        with st.container(border=True):
            st.subheader("Semester Analyzer")
            st.write("Find your semester GPA from your CGPA.")
            if st.button("Go to Analyzer", key="analyzer_nav", use_container_width=True):
                st.session_state.page = "analyzer" # <-- Changed from "cgpa"
                st.rerun()
    
    # Column 3: Future CGPA Predictor
    with col3:
        with st.container(border=True):
            st.subheader("Future CGPA Predictor")
            st.write("See how your next semester will affect your CGPA.")
            if st.button("Go to Predictor", key="predict_nav", use_container_width=True):
                st.session_state.page = "predict"
                st.rerun()


# -----------------------------------------------------------------------------
# Main App Logic (*** UPDATED THIS SECTION ***)
# -----------------------------------------------------------------------------

if "page" not in st.session_state:
    st.session_state.page = "home"

# Page router
if st.session_state.page == "home":
    home_page()
elif st.session_state.page == "gpa":
    gpa_calculator()
elif st.session_state.page == "analyzer": # <-- Changed from "cgpa"
    semester_analyzer()                  # <-- Changed from "cgpa_calculator"
elif st.session_state.page == "predict":
    cgpa_predictor()
