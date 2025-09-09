# lets Import things
import tkinter as tk
import random
import time

# Create the main window
root = tk.Tk()
root.title("Speed Test")
root.config(bg="lightgrey")

# Global variables
start_time = 0
end_time = 0
sentences = [
    "The quick brown fox jumps over the lazy dog.",
    "Python is a powerful programming language.",
    "Typing speed is measured in words per minute.",
    "Practice makes perfect when typing fast.",
]
current_sentence = ""
wpm = 0
accuracy = 0
total_chars = 0
correct_chars = 0
test_running = False

# Function to start the test
def start_test():
    global start_time, current_sentence, test_running, total_chars, correct_chars
    if test_running:
        return
    test_running = True
    total_chars = 0
    correct_chars = 0
    current_sentence = random.choice(sentences)
    sentence_label.config(text=current_sentence)
    input_textbox.delete(0, tk.END)
    start_time = time.time()
    result_label.config(text="")
    wpm_label.config(text="WPM: 0")
    accuracy_label.config(text="Accuracy: 0%")
    start_button.config(state=tk.DISABLED)
    input_textbox.config(state=tk.NORMAL)
    input_textbox.focus()
    root.after(100, check_input)
    status_label.config(text="Status: Test Running", fg="blue")
    timer_label.config(text="Time: 0s")
    update_timer()
    end_button.config(state=tk.NORMAL)
    reset_button.config(state=tk.DISABLED)
    input_textbox.delete(0, tk.END)



# Function to end the test
def end_test():
    global end_time, wpm, accuracy, test_running
    if not test_running:
        return
    end_time = time.time()
    test_running = False
    elapsed_time = end_time - start_time
    total_words = len(current_sentence.split())
    wpm = (total_words / elapsed_time) * 60
    accuracy = (correct_chars / total_chars) * 100 if total_chars > 0 else 0
    result_label.config(text=f"Test Completed! Time: {elapsed_time:.2f}s")
    wpm_label.config(text=f"WPM: {wpm:.2f}")
    accuracy_label.config(text=f"Accuracy: {accuracy:.2f}%")
    start_button.config(state=tk.NORMAL)
    input_textbox.config(state=tk.DISABLED)
    status_label.config(text="Status: Test Ended", fg="green")
    end_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.NORMAL)
    timer_label.config(text="Time: 0s")
    root.after_cancel(update_timer)
    update_timer()
    input_textbox.delete(0, tk.END)

# Function to reset the test
def reset_test():
    global start_time, end_time, current_sentence, wpm, accuracy, total_chars, correct_chars, test_running
    start_time = 0
    end_time = 0
    current_sentence = ""
    wpm = 0
    accuracy = 0
    total_chars = 0
    correct_chars = 0
    test_running = False
    sentence_label.config(text="Click 'Start Test' to begin")
    input_textbox.delete(0, tk.END)
    input_textbox.config(state=tk.DISABLED)
    result_label.config(text="")
    wpm_label.config(text="WPM: 0")
    accuracy_label.config(text="Accuracy: 0%")
    status_label.config(text="Status: Not Running", fg="black")
    timer_label.config(text="Time: 0s")
    start_button.config(state=tk.NORMAL)
    end_button.config(state=tk.DISABLED)
    reset_button.config(state=tk.DISABLED)
    root.after_cancel(update_timer)
    update_timer()
    input_textbox.delete(0, tk.END)


# Function to check input
def check_input():
    global total_chars, correct_chars
    if not test_running:
        return
    user_input = input_textbox.get()
    total_chars = len(user_input)
    correct_chars = sum(1 for i, c in enumerate(user_input) if i < len(current_sentence) and c == current_sentence[i])
    if user_input == current_sentence:
        end_test()
        return
    root.after(100, check_input)
    timer_label.config(text=f"Time: {int(time.time() - start_time)}s")
    update_timer()
# Function to update timer
def update_timer():
    if test_running:
        elapsed_time = int(time.time() - start_time)
        timer_label.config(text=f"Time: {elapsed_time}s")
        root.after(1000, update_timer)
    else:
        timer_label.config(text="Time: 0s")

# UI Elements
title_label = tk.Label(root, text="Speed Test", font=("Helvetica", 20), bg="lightgrey")
title_label.pack(pady=10)

sentence_label = tk.Label(root, text="Click 'Start Test' to begin", font=("Arial", 12), bg="lightgrey", wraplength=350)
sentence_label.pack(pady=10)    

input_textbox = tk.Entry(root, font=("Arial", 12), width=50, state=tk.DISABLED)
input_textbox.pack(pady=10)

result_label = tk.Label(root, text="", font=("Arial", 12), bg="lightgrey")
result_label.pack(pady=5)

wpm_label = tk.Label(root, text="WPM: 0", font=("Arial", 12), bg="lightgrey")
wpm_label.pack(pady=5)

accuracy_label = tk.Label(root, text="Accuracy: 0%", font=("Arial", 12), bg="lightgrey")
accuracy_label.pack(pady=5)

timer_label = tk.Label(root, text="Time: 0s", font=("Arial", 12), bg="lightgrey")
timer_label.pack(pady=5)

status_label = tk.Label(root, text="Status: Not Running", font=("Arial", 12), bg="lightgrey")
status_label.pack(pady=5)

start_button = tk.Button(root, text="Start Test", command=start_test)
start_button.pack(pady=5)

end_button = tk.Button(root, text="End Test", command=end_test, state=tk.DISABLED)
end_button.pack(pady=5)

reset_button = tk.Button(root, text="Reset Test", command=reset_test, state=tk.DISABLED)
reset_button.pack(pady=5)

# Start the main event loop
root.mainloop()