import tkinter as tk

class QuizApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Quiz App")
        self.root.geometry("400x400")

        # Questions Label
        self.questions = [
        {"question": "What is the capital of France?", "options": ["Paris", "London", "Berlin", "Madrid"], "answer": "Paris"},
        {"question": "2 + 2 equals?", "options": ["3", "4", "5", "6"], "answer": "4"},
        {"question": "Python is a...", "options": ["Snake", "Programming Language", "Car", "Movie"], "answer": "Programming Language"},
        ]
        self.current_question = 0
        self.score = 0

        # Question Label 
        self.question_Label = tk.Label(root, text="", font=("Arial", 14), wraplength=350)
        self.question_Label.pack(pady=20)

        # Variable for selected option
        self.questions_var = tk.StringVar()

        # Option Buttons
        self.option_buttons = []
        for i in range(4):
            rb = tk.Radiobutton(root, text="", variable=self.questions_var, value="", font=("Arial", 12))
            rb.pack(anchor="w")
            self.option_buttons.append(rb)
        
        # Navigation buttons
        btn_frame = tk.Frame(root)
        btn_frame.pack(pady=20)
        self.prev_btn = tk.Button(btn_frame, text="Previous", command=self.prev_question)
        self.prev_btn.grid(row=0, column=0, padx=10)
        self.next_btn = tk.Button(btn_frame, text="Next", command=self.next_question)
        self.next_btn.grid(row=0, column=1, padx=10)

        # Result label
        self.result_label = tk.Label(root, font=("Arial", 12))
        self.result_label.pack()
        self.load_question()

    def load_question(self):
        q = self.questions[self.current_question]
        self.question_Label.config(text=q["question"])
        self.questions_var.set(None)
        for i, option in enumerate(q["options"]):
            self.option_buttons[i].config(text=option, value=option)
            self.result_label.config(text="")
            self.update_navigation_buttons()

    def update_navigation_buttons(self):
        self.prev_btn.config(state="normal" if self.current_question > 0 else "disabled")
        self.next_btn.config(text="Submit" if self.current_question == len(self.questions)-1 else "Next")

    def next_question(self):
        if not self.questions_var.get():
            self.result_label.config(text="Please select an option.")
            return
        correct_answer = self.questions[self.current_question]["answer"]
        if self.questions_var.get() == correct_answer:
            self.score += 1
        if self.current_question < len(self.questions) - 1:
            self.current_question += 1
            self.load_question()
        else:
            self.show_result()
    def prev_question(self):
        if self.current_question > 0:
            self.current_question -= 1
            self.load_question()

    def show_result(self):
        self.question_Label.pack_forget()
        for rb in self.option_buttons:
            rb.pack_forget()
            self.prev_btn.pack_forget()
            self.next_btn.pack_forget()
            self.result_label.config(text=f"Quiz Completed! Your score: {self.score}/{len(self.questions)}")
# ✅ Run only once
if __name__ == "__main__":
    root = tk.Tk()
    app = QuizApp(root)
    root.mainloop()