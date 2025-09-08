import tkinter

root = tkinter.Tk()
# Student ID label and textbox
student_id_Label = tkinter.Label(root, text = "Enter Student ID")
student_id_Label.pack()
student_id_Textbox = tkinter.Entry(root)
student_id_Textbox.pack()

# Student Name label and textbox
student_name_Label = tkinter.Label(root, text = "Enter Student Name")
student_name_Label.pack()
student_name_Textbox = tkinter.Entry(root)
student_name_Textbox.pack()

# Student Email label and textbox
student_email_Label = tkinter.Label(root, text = "Enter Student Email")
student_email_Label.pack()
student_email_Textbox = tkinter.Entry(root)
student_email_Textbox.pack()

# Student Phone label and textbox
student_phone_Label = tkinter.Label(root, text = "Enter Student Phone Number")
student_phone_Label.pack()
student_phone_Textbox = tkinter.Entry(root)
student_phone_Textbox.pack()
# Submit button
submit_button = tkinter.Button(root, text = "Submit")
submit_button.pack()
root.mainloop()