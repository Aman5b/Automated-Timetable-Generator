import streamlit as st
import sqlite3
import base64
import pandas as pd
import random

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


st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Generate Time Table"}</h1>', unsafe_allow_html=True)

if st.button("Generate"):


# # ==================================================================




    gen = st.radio("ODD/Even",["ODD Sem", "Even Sem"],index=0)
    

    st.markdown(f'<h1 style="color:#000000;text-align: center;font-size:20px;">{"Generate Time Table"}</h1>', unsafe_allow_html=True)
    if gen == "ODD Sem":
        
        if st.button("Generate"):
            temp = [1,3,5,7]
            for ii in range(0,4):
                st.write('Sem : ',temp[ii])
                st.write('Room Number : ',temp[ii]+random.randint(1, 9))
                
                # Simplified logic for timetable generation
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                times = ["08:30-09:30","09:30-10:30", "10:30-11:30", "11:30-12:30","12:30-01:30",
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
                            subject = subject_df.sample(n=1).iloc[0]["Subject Name"]
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
                            
                st.success('Sem : '+str(temp[ii])+"  - Timetable Generated Successfully!")        
            

    if gen == "Even Sem":



        if st.button("Generate"):
            temp = [2,4,6,8]
            for ii in range(0,4):
                
                st.write('Sem : ',temp[ii])
                st.write('Room Number : ',temp[ii]+random.randint(1, 9))

                # Simplified logic for timetable generation
                days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]
                times = ["08:30-09:30","09:30-10:30", "10:30-11:30", "11:30-12:30","12:30-01:30",
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
                            
                            subject_df = pd.read_csv("subs_df.csv")
                            subject = subject_df.sample(n=1).iloc[0]["Subject Name"]
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
                            
                st.success('Sem : '+str(temp[ii])+"  - Timetable Generated Successfully!")     