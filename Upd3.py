import streamlit as st
import pandas as pd
import base64
import random
from genetictabler import GenerateTimeTable



# Set up the app title and background
st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:36px;">{"Automatic Time Table Generator"}</h1>', unsafe_allow_html=True)

def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )
add_bg_from_local('1.jpg')

menu = ["Add Room", "Add Lab", "Add Teacher", "Add Semester", "Add Department", "Add Subjects", "Add Sections", "Generate Timetable"] 
choice = st.selectbox("Menu", menu)

# Define the "Add Room" section
if choice == "Add Room":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Room"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the rooms DataFrame
    try:
        rooms_df = pd.read_csv("rooms_df.csv")
    except FileNotFoundError:
        rooms_df = pd.DataFrame(columns=["Room Name", "Capacity"])

    # User inputs
    room_name = st.text_input("Room Name")
    capacity = st.number_input("Capacity", min_value=1, step=1)

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing room
    if action in ["Edit", "Delete"]:
        if not rooms_df.empty:
            selected_room = st.selectbox("Select Room", rooms_df["Room Name"].values)
            if action == "Edit":
                room_details = rooms_df[rooms_df["Room Name"] == selected_room]
                if not room_details.empty:
                    room_name = st.text_input("Edit Room Name", room_details["Room Name"].values[0])
                    capacity = st.number_input("Edit Capacity", min_value=1, step=1, value=int(room_details["Capacity"].values[0]))
        else:
            st.warning("No rooms available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_room = pd.DataFrame({"Room Name": [room_name], "Capacity": [capacity]})
            rooms_df = pd.concat([rooms_df, new_room], ignore_index=True)
            st.success("Room Added Successfully!")
        elif action == "Edit" and not rooms_df.empty:
            rooms_df.loc[rooms_df["Room Name"] == selected_room, "Room Name"] = room_name
            rooms_df.loc[rooms_df["Room Name"] == selected_room, "Capacity"] = capacity
            st.success("Room Edited Successfully!")
        elif action == "Delete" and not rooms_df.empty:
            rooms_df = rooms_df[rooms_df["Room Name"] != selected_room]
            st.success("Room Deleted Successfully!")

        # Save the updated DataFrame and display it
        rooms_df.to_csv('rooms_df.csv', index=False)
        st.table(rooms_df)

# Define the "Add Lab" section
elif choice == "Add Lab":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Lab"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the labs DataFrame
    try:
        labs_df = pd.read_csv("labs_df.csv")
    except FileNotFoundError:
        labs_df = pd.DataFrame(columns=["Lab Name", "Capacity"])

    # User inputs
    lab_name = st.text_input("Lab Name")
    capacity = st.number_input("Capacity", min_value=1, step=1)

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing lab
    if action in ["Edit", "Delete"]:
        if not labs_df.empty:
            selected_lab = st.selectbox("Select Lab", labs_df["Lab Name"].values)
            if action == "Edit":
                lab_details = labs_df[labs_df["Lab Name"] == selected_lab]
                if not lab_details.empty:
                    lab_name = st.text_input("Edit Lab Name", lab_details["Lab Name"].values[0])
                    capacity = st.number_input("Edit Capacity", min_value=1, step=1, value=int(lab_details["Capacity"].values[0]))
        else:
            st.warning("No labs available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_lab = pd.DataFrame({"Lab Name": [lab_name], "Capacity": [capacity]})
            labs_df = pd.concat([labs_df, new_lab], ignore_index=True)
            st.success("Lab Added Successfully!")
        elif action == "Edit" and not labs_df.empty:
            labs_df.loc[labs_df["Lab Name"] == selected_lab, "Lab Name"] = lab_name
            labs_df.loc[labs_df["Lab Name"] == selected_lab, "Capacity"] = capacity
            st.success("Lab Edited Successfully!")
        elif action == "Delete" and not labs_df.empty:
            labs_df = labs_df[labs_df["Lab Name"] != selected_lab]
            st.success("Lab Deleted Successfully!")

        # Save the updated DataFrame and display it
        labs_df.to_csv('labs_df.csv', index=False)
        st.table(labs_df)

# Define the "Add Teacher" section
elif choice == "Add Teacher":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Teacher"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the teachers DataFrame
    try:
        teachers_df = pd.read_csv("teachers_df.csv")
    except FileNotFoundError:
        teachers_df = pd.DataFrame(columns=["Teacher Name", "Subjects Taught"])

    # User inputs
    teacher_name = st.text_input("Teacher Name")
    subjects_taught = st.text_input("Subjects Taught (comma-separated)")

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing teacher
    if action in ["Edit", "Delete"]:
        if not teachers_df.empty:
            selected_teacher = st.selectbox("Select Teacher", teachers_df["Teacher Name"].values)
            if action == "Edit":
                teacher_details = teachers_df[teachers_df["Teacher Name"] == selected_teacher]
                if not teacher_details.empty:
                    teacher_name = st.text_input("Edit Teacher Name", teacher_details["Teacher Name"].values[0])
                    subjects_taught = st.text_input("Edit Subjects Taught (comma-separated)", teacher_details["Subjects Taught"].values[0])
        else:
            st.warning("No teachers available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_teacher = pd.DataFrame({"Teacher Name": [teacher_name], "Subjects Taught": [subjects_taught]})
            teachers_df = pd.concat([teachers_df, new_teacher], ignore_index=True)
            st.success("Teacher Added Successfully!")
        elif action == "Edit" and not teachers_df.empty:
            teachers_df.loc[teachers_df["Teacher Name"] == selected_teacher, "Teacher Name"] = teacher_name
            teachers_df.loc[teachers_df["Teacher Name"] == selected_teacher, "Subjects Taught"] = subjects_taught
            st.success("Teacher Edited Successfully!")
        elif action == "Delete" and not teachers_df.empty:
            teachers_df = teachers_df[teachers_df["Teacher Name"] != selected_teacher]
            st.success("Teacher Deleted Successfully!")

        # Save the updated DataFrame and display it
        teachers_df.to_csv('teachers_df.csv', index=False)
        st.table(teachers_df)

# Define the "Add Semester" section
elif choice == "Add Semester":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Semester"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the semesters DataFrame
    try:
        semesters_df = pd.read_csv("semesters_df.csv")
    except FileNotFoundError:
        semesters_df = pd.DataFrame(columns=["Semester Name", "Department", "Sections", "Even/Odd"])

    # User inputs
    semester_name = st.text_input("Semester Name")
    department = st.text_input("Department")
    sections = st.text_input("Sections (comma-separated)")
    even_odd = st.radio("Even/Odd Semester", ["Even", "Odd"])

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing semester
    if action in ["Edit", "Delete"]:
        if not semesters_df.empty:
            selected_semester = st.selectbox("Select Semester", semesters_df["Semester Name"].values)
            if action == "Edit":
                semester_details = semesters_df[semesters_df["Semester Name"] == selected_semester]
                if not semester_details.empty:
                    semester_name = st.text_input("Edit Semester Name", semester_details["Semester Name"].values[0])
                    department = st.text_input("Edit Department", semester_details["Department"].values[0])
                    sections = st.text_input("Edit Sections (comma-separated)", semester_details["Sections"].values[0])
                    even_odd = st.radio("Edit Even/Odd Semester", ["Even", "Odd"], index=0 if semester_details["Even/Odd"].values[0] == "Even" else 1)
        else:
            st.warning("No semesters available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_semester = pd.DataFrame({"Semester Name": [semester_name], "Department": [department], "Sections": [sections], "Even/Odd": [even_odd]})
            semesters_df = pd.concat([semesters_df, new_semester], ignore_index=True)
            st.success("Semester Added Successfully!")
        elif action == "Edit" and not semesters_df.empty:
            semesters_df.loc[semesters_df["Semester Name"] == selected_semester, "Semester Name"] = semester_name
            semesters_df.loc[semesters_df["Semester Name"] == selected_semester, "Department"] = department
            semesters_df.loc[semesters_df["Semester Name"] == selected_semester, "Sections"] = sections
            semesters_df.loc[semesters_df["Semester Name"] == selected_semester, "Even/Odd"] = even_odd
            st.success("Semester Edited Successfully!")
        elif action == "Delete" and not semesters_df.empty:
            semesters_df = semesters_df[semesters_df["Semester Name"] != selected_semester]
            st.success("Semester Deleted Successfully!")

        # Save the updated DataFrame and display it
        semesters_df.to_csv('semesters_df.csv', index=False)
        st.table(semesters_df)

# Define the "Add Department" section
elif choice == "Add Department":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Department"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the departments DataFrame
    try:
        departments_df = pd.read_csv("departments_df.csv")
    except FileNotFoundError:
        departments_df = pd.DataFrame(columns=["Department Name", "HOD"])

    # User inputs
    department_name = st.text_input("Department Name")
    hod = st.text_input("HOD")

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing department
    if action in ["Edit", "Delete"]:
        if not departments_df.empty:
            selected_department = st.selectbox("Select Department", departments_df["Department Name"].values)
            if action == "Edit":
                department_details = departments_df[departments_df["Department Name"] == selected_department]
                if not department_details.empty:
                    department_name = st.text_input("Edit Department Name", department_details["Department Name"].values[0])
                    hod = st.text_input("Edit HOD", department_details["HOD"].values[0])
        else:
            st.warning("No departments available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_department = pd.DataFrame({"Department Name": [department_name], "HOD": [hod]})
            departments_df = pd.concat([departments_df, new_department], ignore_index=True)
            st.success("Department Added Successfully!")
        elif action == "Edit" and not departments_df.empty:
            departments_df.loc[departments_df["Department Name"] == selected_department, "Department Name"] = department_name
            departments_df.loc[departments_df["Department Name"] == selected_department, "HOD"] = hod
            st.success("Department Edited Successfully!")
        elif action == "Delete" and not departments_df.empty:
            departments_df = departments_df[departments_df["Department Name"] != selected_department]
            st.success("Department Deleted Successfully!")

        # Save the updated DataFrame and display it
        departments_df.to_csv('departments_df.csv', index=False)
        st.table(departments_df)

# Define the "Add Subjects" section
elif choice == "Add Subjects":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Subjects"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the subjects DataFrame
    try:
        subjects_df = pd.read_csv("subjects_df.csv")
    except FileNotFoundError:
        subjects_df = pd.DataFrame(columns=["Subject Name", "Semester", "Department"])
    
    subjects_df.to_csv('subs_df.csv', index=False)

    # User inputs
    subject_name = st.text_input("Subject Name")
    semester = st.text_input("Semester")
    department = st.text_input("Department")

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing subject
    if action in ["Edit", "Delete"]:
        if not subjects_df.empty:
            selected_subject = st.selectbox("Select Subject", subjects_df["Subject Name"].values)
            if action == "Edit":
                subject_details = subjects_df[subjects_df["Subject Name"] == selected_subject]
                if not subject_details.empty:
                    subject_name = st.text_input("Edit Subject Name", subject_details["Subject Name"].values[0])
                    semester = st.text_input("Edit Semester", subject_details["Semester"].values[0])
                    department = st.text_input("Edit Department", subject_details["Department"].values[0])
        else:
            st.warning("No subjects available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_subject = pd.DataFrame({"Subject Name": [subject_name], "Semester": [semester], "Department": [department]})
            subjects_df = pd.concat([subjects_df, new_subject], ignore_index=True)
            st.success("Subject Added Successfully!")
        elif action == "Edit" and not subjects_df.empty:
            subjects_df.loc[subjects_df["Subject Name"] == selected_subject, "Subject Name"] = subject_name
            subjects_df.loc[subjects_df["Subject Name"] == selected_subject, "Semester"] = semester
            subjects_df.loc[subjects_df["Subject Name"] == selected_subject, "Department"] = department
            st.success("Subject Edited Successfully!")
        elif action == "Delete" and not subjects_df.empty:
            subjects_df = subjects_df[subjects_df["Subject Name"] != selected_subject]
            st.success("Subject Deleted Successfully!")

        # Save the updated DataFrame and display it
        subjects_df.to_csv('subjects_df.csv', index=False)
        st.table(subjects_df)

# Define the "Add Sections" section
elif choice == "Add Sections":
    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Add Sections"}</h1>', unsafe_allow_html=True)
    
    # Load or initialize the sections DataFrame
    try:
        sections_df = pd.read_csv("sections_df.csv")
    except FileNotFoundError:
        sections_df = pd.DataFrame(columns=["Section Name", "Semester", "Department"])

    # User inputs
    section_name = st.text_input("Section Name")
    semester = st.text_input("Semester")
    department = st.text_input("Department")

    # Select the action (Add, Edit, Delete)
    action = st.selectbox("Action", ["Add", "Edit", "Delete"])

    # If Edit or Delete, select the existing section
    if action in ["Edit", "Delete"]:
        if not sections_df.empty:
            selected_section = st.selectbox("Select Section", sections_df["Section Name"].values)
            if action == "Edit":
                section_details = sections_df[sections_df["Section Name"] == selected_section]
                if not section_details.empty:
                    section_name = st.text_input("Edit Section Name", section_details["Section Name"].values[0])
                    semester = st.text_input("Edit Semester", section_details["Semester"].values[0])
                    department = st.text_input("Edit Department", section_details["Department"].values[0])
        else:
            st.warning("No sections available to edit or delete.")

    # Perform the selected action
    if st.button(action):
        if action == "Add":
            new_section = pd.DataFrame({"Section Name": [section_name], "Semester": [semester], "Department": [department]})
            sections_df = pd.concat([sections_df, new_section], ignore_index=True)
            st.success("Section Added Successfully!")
        elif action == "Edit" and not sections_df.empty:
            sections_df.loc[sections_df["Section Name"] == selected_section, "Section Name"] = section_name
            sections_df.loc[sections_df["Section Name"] == selected_section, "Semester"] = semester
            sections_df.loc[sections_df["Section Name"] == selected_section, "Department"] = department
            st.success("Section Edited Successfully!")
        elif action == "Delete" and not sections_df.empty:
            sections_df = sections_df[sections_df["Section Name"] != selected_section]
            st.success("Section Deleted Successfully!")

        # Save the updated DataFrame and display it
        sections_df.to_csv('sections_df.csv', index=False)
        st.table(sections_df)

# ==================================================================




elif choice == "Generate Timetable":
    gen = st.radio("ODD/Even",["ODD Sem", "Even Sem"],index=0)
    

    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Generate Time Table"}</h1>', unsafe_allow_html=True)
    if gen == "ODD Sem":
        subjectttt = []
        if st.button("Generate"):
            temp = [1,3,5,7]
            for ii in range(0,4):
                st.write('Sem : ',temp[ii])
                import pandas as pd
                roomm = pd.read_csv("rooms_df.csv")
                roomm_name = roomm['Room Name'][ii]
                
                # st.write('Room Number : ',temp[ii]+random.randint(1, 9))
                st.write('Room Number :'  ,roomm_name )
                
                # Simplified logic for timetable generation
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                times = ["09:30-10:30", "10:30-11:30", "11:30-12:30","12:30-01:30",
                         "1:30-2:30", "2:30-3:30", "3:30-4:30", "4:30-5:30"]
                sections_df = pd.read_csv("sections_df.csv")
                rooms_df = pd.read_csv("rooms_df.csv")
                labs_df = pd.read_csv("labs_df.csv")
        
                final_res = []
        
                for day in days:
                    for time in times:
                        for index, row in sections_df.iterrows():
                            semester = row["Semester"]
                            section = row["Section Name"]
                            # teachers_df = pd.read_csv("teachers_df.csv")
                            # teacher = teachers_df.sample(n=1).iloc[0]["Teacher Name"]
                            room = rooms_df.sample(n=1).iloc[0]["Room Name"]
                            labs = labs_df.sample(n=1).iloc[0]["Lab Name"]
                            
                            subject_df = pd.read_csv("subjects_df.csv")
                            if temp[ii] == 1:
                                tt = subject_df['Semester'] == 'ONE'
                            if temp[ii] == 3:
                                tt = subject_df['Semester'] == 'THREE'
                                
                            if temp[ii] == 5:
                                tt = subject_df['Semester'] == 'FIVE'
                                
                            if temp[ii] == 7:
                                tt = subject_df['Semester'] == 'SEVEN'
                            res = [am for am, val in enumerate(tt) if val]
                                # subject = subject_df.sample(n=1).iloc[0]["Subject Name"]
                            subjectttt = []
                            for amd in range(0,len(res)):
                                subjectttt.append(subject_df['Subject Name'][res[amd]])
                            
                            subject = subjectttt[random.randint(0,len(res))-1]
                                
                            if time == '12:30-01:30':
                                new_entry = {
                                    "Day": day,
                                    "Time": time,
                                    "Room/Lab": "",
                                    "Lab": "",
            
                                    "Subject": "LUNCH",
                                    "Semester": "LUNCH",
                                    "Section": "LUNCH"
                                }
                            else:
                                new_entry = {
                                    "Day": day,
                                    "Time": time,
                                    "Room/Lab": room,
                                    "Lab": labs,
            
                                    "Subject": subject,
                                    "Semester": semester,
                                    "Section": section
                                }
                            final_res.append(new_entry)
        
                timetable_df = pd.DataFrame(final_res)
        
                # Ensure days are in the correct order
                day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                timetable_df['Day'] = pd.Categorical(timetable_df['Day'], categories=day_order, ordered=True)
                
                        
                # timetable_df['Combined'] = timetable_df.apply(
                #     lambda row: f"{row['Lab']}\n{row['Subject']}" if pd.notna(row['Lab']) else f"{row['Room/Lab']}\n{row['Subject']}",
                #     axis=1
                # )
                
                def combine_information(row):
                    # if row.name == len(timetable_df) - 1 and pd.notna(row['Lab']):
                    #     return f"{row['Lab']}\n{row['Subject']}"
                    # if row.name == len(timetable_df) - 2 and pd.notna(row['Lab']):
                    #     return f"{row['Lab']}\n{row['Subject']}"
                    # if row.name == len(timetable_df) - 3 and pd.notna(row['Lab']):
                    #     return f"{row['Lab']}\n{row['Subject']}"
                    
                    
                    if row.name == 1 and pd.notna(row['Lab']):
                        return f"{row['Subject']}" 
                    if row.name == 2 and pd.notna(row['Lab']):
                        return f"{row['Subject']}" 
                    
                    
                    if row.name == 9 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 10 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"
                     
                        
                    if row.name == 17 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 18 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    
                    
                    if row.name == 25 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 26 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
        
        
                    if row.name == 33 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 34 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"
        
                    
                    elif pd.notna(row['Lab']):
                        return f"{row['Subject']}"
                    else:
                        return f"{row['Subject']}"
                
                timetable_df['Combined'] = timetable_df.apply(combine_information, axis=1)
        
        
                # Pivot the DataFrame to have days as columns and times as rows
                pivot_table = timetable_df.pivot(index="Time", columns="Day", values="Combined")
        
                # Format the table to have days as columns and times as rows with combined information
                pivot_table = pivot_table[day_order]
        
                # Display the formatted timetable
                st.write(pivot_table)
                pivot_table.to_csv('final_timetable.csv')
                
                total_classes = 6
                no_courses = 6
                slots = 6
                total_days = 6
                daily_repetition = 3
                
                table = GenerateTimeTable(total_classes, no_courses, slots, total_days, daily_repetition)
                for single_table in table.run():
                    for days in single_table:
                        print(days)
                    print("-----------------------------------")
                            
                st.success('Sem : '+str(temp[ii])+"  - Timetable Generated Successfully!")        
            

    if gen == "Even Sem":



        if st.button("Generate"):
            temp = [2,4,6]
            for ii in range(0,3):
                
                st.write('Sem : ',temp[ii])
                st.write('Room Number : ',temp[ii]+random.randint(1, 9))

                # Simplified logic for timetable generation
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                times = ["09:30-10:30", "10:30-11:30", "11:30-12:30","12:30-01:30",
                         "1:30-2:30", "2:30-3:30", "3:30-4:30", "4:30-5:30"]
                sections_df = pd.read_csv("sections_df.csv")
                rooms_df = pd.read_csv("rooms_df.csv")
                labs_df = pd.read_csv("labs_df.csv")
        
                final_res = []
        
                for day in days:
                    for time in times:
                        for index, row in sections_df.iterrows():
                            semester = row["Semester"]
                            section = row["Section Name"]
                            # teachers_df = pd.read_csv("teachers_df.csv")
                            # teacher = teachers_df.sample(n=1).iloc[0]["Teacher Name"]
                            room = rooms_df.sample(n=1).iloc[0]["Room Name"]
                            labs = labs_df.sample(n=1).iloc[0]["Lab Name"]
                            
                            subject_df = pd.read_csv("subjects_df.csv")
                            if temp[ii] == 2:
                                tt = subject_df['Semester'] == 'TWO'
                            if temp[ii] == 4:
                                tt = subject_df['Semester'] == 'FOUR'
                                
                            if temp[ii] == 6:
                                tt = subject_df['Semester'] == 'SIX'
                                
                            # if temp[ii] == 8:
                            #     tt = subject_df['Semester'] == 'EIGHT'

                                 
                            res = [am for am, val in enumerate(tt) if val]
                                # subject = subject_df.sample(n=1).iloc[0]["Subject Name"]
                            subjectttt = []
                            for amd in range(0,len(res)):
                                subjectttt.append(subject_df['Subject Name'][res[amd]])
                            
                            subject = subjectttt[random.randint(0,len(res))-1]
                                
                            if time == '12:30-01:30':
                                new_entry = {
                                    "Day": day,
                                    "Time": time,
                                    "Room/Lab": "",
                                    "Lab": "",
            
                                    "Subject": "LUNCH",
                                    "Semester": "LUNCH",
                                    "Section": "LUNCH"
                                }
                            else:
                                new_entry = {
                                    "Day": day,
                                    "Time": time,
                                    "Room/Lab": room,
                                    "Lab": labs,
            
                                    "Subject": subject,
                                    "Semester": semester,
                                    "Section": section
                                }
                            final_res.append(new_entry)
        
                timetable_df = pd.DataFrame(final_res)
        
                # Ensure days are in the correct order
                day_order = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                timetable_df['Day'] = pd.Categorical(timetable_df['Day'], categories=day_order, ordered=True)
                
                        
                        
                # timetable_df['Combined'] = timetable_df.apply(
                #     lambda row: f"{row['Lab']}\n{row['Subject']}" if pd.notna(row['Lab']) else f"{row['Room/Lab']}\n{row['Subject']}",
                #     axis=1
                # )
                
                def combine_information(row):
                    # if row.name == len(timetable_df) - 1 and pd.notna(row['Lab']):
                    #     return f"{row['Lab']}\n{row['Subject']}"
                    # if row.name == len(timetable_df) - 2 and pd.notna(row['Lab']):
                    #     return f"{row['Lab']}\n{row['Subject']}"
                    # if row.name == len(timetable_df) - 3 and pd.notna(row['Lab']):
                    #     return f"{row['Lab']}\n{row['Subject']}"
                    
                    
                    if row.name == 1 and pd.notna(row['Lab']):
                        return f"{row['Subject']}" 
                    if row.name == 2 and pd.notna(row['Lab']):
                        return f"{row['Subject']}" 
                    
                    
                    if row.name == 9 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 10 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"
                     
                        
                    if row.name == 17 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 18 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    
                    
                    if row.name == 25 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 26 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
        
        
                    if row.name == 33 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"             
                    if row.name == 34 and pd.notna(row['Lab']):
                        return f"{row['Subject']}"
        
                    
                    elif pd.notna(row['Lab']):
                        return f"{row['Subject']}"
                    else:
                        return f"{row['Subject']}"
                
                timetable_df['Combined'] = timetable_df.apply(combine_information, axis=1)
        
        
                # Pivot the DataFrame to have days as columns and times as rows
                pivot_table = timetable_df.pivot(index="Time", columns="Day", values="Combined")
        
                # Format the table to have days as columns and times as rows with combined information
                pivot_table = pivot_table[day_order]
        
                # Display the formatted timetable
                st.write(pivot_table)
                pivot_table.to_csv('final_timetable.csv')
                
                total_classes = 6
                no_courses = 6
                slots = 6
                total_days = 6
                daily_repetition = 3
                
                table = GenerateTimeTable(total_classes, no_courses, slots, total_days, daily_repetition)
                for single_table in table.run():
                    for days in single_table:
                        print(days)
                    print("-----------------------------------")
                            
                st.success('Sem : '+str(temp[ii])+"  - Timetable Generated Successfully!")        
# ==================================================================
