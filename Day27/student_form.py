# import tkinter 
# from tkinter import messagebox
# import openpyxl 

# filepath = "D:\\V-TechnoSolutions\\PythonFullstack\\Day27\\Testing.xlsx"
# A = openpyxl.load_workbook(filepath)
# # If sheet "Testing" exists, use it. Otherwise, create it.
# if "Testing" in A.sheetnames:
#     B = A["Testing"]
# else:
#     B = A.create_sheet("Testing")

# print(B)
# def onclick():
#     student_id = student_id_Textbox.get()
#     student_name = student_name_Textbox.get()
#     student_email = student_email_Textbox.get()
#     student_phone = student_phone_Textbox.get()
    
#     if student_id and student_name and student_email and student_phone:
#         # Append row to worksheet
#         B.append([student_id, student_name, student_email, student_phone])
#         # Save workbook
#         A.save(filepath)
#         # Clear textboxes
#         student_id_Textbox.delete(0, tkinter.END)
#         student_name_Textbox.delete(0, tkinter.END)
#         student_email_Textbox.delete(0, tkinter.END)
#         student_phone_Textbox.delete(0, tkinter.END)
#         messagebox.showinfo("Information", "Student Registered Successfully")
#     else:
#         messagebox.showwarning("Warning", "Please fill all the fields")

# root = tkinter.Tk()
# root.geometry("400x400")
# root.title("Student Registration Form")

# # Student ID
# student_id_Label = tkinter.Label(root, text="Enter Student ID")
# student_id_Label.pack(anchor=tkinter.W, padx=10)
# student_id_Textbox = tkinter.Entry(root)
# student_id_Textbox.pack(anchor=tkinter.W, padx=10)

# # Student Name
# student_name_Label = tkinter.Label(root, text="Enter Student Name")
# student_name_Label.pack(anchor=tkinter.W, padx=10)
# student_name_Textbox = tkinter.Entry(root)
# student_name_Textbox.pack(anchor=tkinter.W, padx=10)

# # Student Email
# student_email_Label = tkinter.Label(root, text="Enter Student Email")
# student_email_Label.pack(anchor=tkinter.W, padx=10)
# student_email_Textbox = tkinter.Entry(root)
# student_email_Textbox.pack(anchor=tkinter.W, padx=10)

# # Student Phone
# student_phone_Label = tkinter.Label(root, text="Enter Student Phone Number")
# student_phone_Label.pack(anchor=tkinter.W, padx=10)
# student_phone_Textbox = tkinter.Entry(root)
# student_phone_Textbox.pack(anchor=tkinter.W, padx=10)

# # Submit button (fixed)
# submit_button = tkinter.Button(root, text="Submit", command=onclick)
# submit_button.pack(anchor=tkinter.W, padx=10)

# root.mainloop()


import tkinter
from tkinter import messagebox
import json
import os

file_path = "students.json"

# Ensure the JSON file exists
if not os.path.exists(file_path):
    with open(file_path, "w") as f:
        json.dump([], f)  # start with an empty list

root = tkinter.Tk()
root.geometry("300x400")
root.title("Student Registration Form")

def onClick_Submit():
    name = name_textbox.get()
    email = email_textbox.get()
    phone = phone_textbox.get()

    if name and email and phone:
        # Load existing data
        with open(file_path, "r") as f:
            students = json.load(f)

        # Add new student entry
        students.append({
            "name": name,
            "email": email,
            "phone": phone
        })

        # Save back to JSON
        with open(file_path, "w") as f:
            json.dump(students, f, indent=4)

        messagebox.showinfo("Status", "Data Submitted and Saved in JSON")

        # Clear textboxes
        name_textbox.delete(0, tkinter.END)
        email_textbox.delete(0, tkinter.END)
        phone_textbox.delete(0, tkinter.END)

    else:
        messagebox.showwarning("Warning", "Please fill all the fields")

# GUI Layout
name_label = tkinter.Label(root, text="Enter Name")
name_label.pack(anchor=tkinter.W, padx=10)
name_textbox = tkinter.Entry(root)
name_textbox.pack(anchor=tkinter.W, padx=10)

email_label = tkinter.Label(root, text="Enter Email")
email_label.pack(anchor=tkinter.W, padx=10)
email_textbox = tkinter.Entry(root)
email_textbox.pack(anchor=tkinter.W, padx=10)

phone_label = tkinter.Label(root, text="Enter Phone Number")
phone_label.pack(anchor=tkinter.W, padx=10)
phone_textbox = tkinter.Entry(root)
phone_textbox.pack(anchor=tkinter.W, padx=10)

Submit_button = tkinter.Button(root, text='Submit', command=onClick_Submit)
Submit_button.pack(anchor=tkinter.W, padx=10, pady=10)

root.mainloop()
