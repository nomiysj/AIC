import tkinter as tk
from tkinter import messagebox

class ITSApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Intelligent Tutoring System")
        self.root.geometry("600x400")
        self.root.config(bg="#f5f5f5")

        # Main Title Label with Style
        self.title_label = tk.Label(self.root, text="Welcome to the Intelligent Tutoring System", font=("Arial", 18, 'bold'), fg="#2c3e50", bg="#f5f5f5")
        self.title_label.pack(pady=30)

        # Button Styling
        self.button_style = {'width': 20, 'height': 2, 'font': ('Arial', 12, 'bold'), 'bg': "#3498db", 'fg': "white", 'bd': 0, 'relief': 'flat'}

        # Start Lesson Button
        self.lesson_button = tk.Button(self.root, text="Start Lesson", **self.button_style, command=self.start_lesson)
        self.lesson_button.pack(pady=10)

        # Take Quiz Button
        self.quiz_button = tk.Button(self.root, text="Take Quiz", **self.button_style, command=self.take_quiz)
        self.quiz_button.pack(pady=10)

        # Feedback Section
        self.feedback_label = tk.Label(self.root, text="Feedback: None", font=("Arial", 12), fg="#34495e", bg="#f5f5f5")
        self.feedback_label.pack(pady=20)

        # Exit Button
        self.exit_button = tk.Button(self.root, text="Exit", width=10, height=2, font=('Arial', 12), bg="#e74c3c", fg="white", command=self.root.quit)
        self.exit_button.pack(pady=10)

    def start_lesson(self):
        # New Window for Lesson
        lesson_window = tk.Toplevel(self.root)
        lesson_window.title("Lesson - Area Calculation")
        lesson_window.geometry("400x300")
        lesson_window.config(bg="#ecf0f1")

        # Lesson Title
        lesson_text = tk.Label(lesson_window, text="Lesson: Calculate the area of a rectangle.", font=("Arial", 14, 'bold'), fg="#2c3e50", bg="#ecf0f1")
        lesson_text.pack(pady=20)

        # Length and Width Inputs
        self.length_label = tk.Label(lesson_window, text="Enter Length: ", font=("Arial", 12), fg="#2c3e50", bg="#ecf0f1")
        self.length_label.pack()
        self.length_entry = tk.Entry(lesson_window, font=("Arial", 12), bd=2)
        self.length_entry.pack(pady=5)

        self.width_label = tk.Label(lesson_window, text="Enter Width: ", font=("Arial", 12), fg="#2c3e50", bg="#ecf0f1")
        self.width_label.pack()
        self.width_entry = tk.Entry(lesson_window, font=("Arial", 12), bd=2)
        self.width_entry.pack(pady=5)

        # Calculate Button
        self.submit_button = tk.Button(lesson_window, text="Calculate Area", font=("Arial", 12, 'bold'), bg="#27ae60", fg="white", command=self.calculate_area)
        self.submit_button.pack(pady=10)

    def calculate_area(self):
        try:
            length = float(self.length_entry.get())
            width = float(self.width_entry.get())
            area = length * width
            self.feedback_label.config(text=f"Feedback: Correct! The area is {area} square units.", fg="#27ae60")
        except ValueError:
            self.feedback_label.config(text="Feedback: Invalid input. Please enter valid numbers.", fg="#e74c3c")

    def take_quiz(self):
        # Quiz Window
        quiz_window = tk.Toplevel(self.root)
        quiz_window.title("Quiz - Area Calculation")
        quiz_window.geometry("400x300")
        quiz_window.config(bg="#ecf0f1")

        quiz_text = tk.Label(quiz_window, text="Quiz: What is the area of a 5x10 rectangle?", font=("Arial", 14, 'bold'), fg="#2c3e50", bg="#ecf0f1")
        quiz_text.pack(pady=20)

        # Answer Input
        self.answer_label = tk.Label(quiz_window, text="Enter your answer: ", font=("Arial", 12), fg="#2c3e50", bg="#ecf0f1")
        self.answer_label.pack()
        self.answer_entry = tk.Entry(quiz_window, font=("Arial", 12), bd=2)
        self.answer_entry.pack(pady=5)

        # Submit Button for Quiz
        self.submit_button_quiz = tk.Button(quiz_window, text="Submit Answer", font=("Arial", 12, 'bold'), bg="#f39c12", fg="white", command=self.check_answer)
        self.submit_button_quiz.pack(pady=10)

    def check_answer(self):
        try:
            answer = float(self.answer_entry.get())
            if answer == 50:
                messagebox.showinfo("Correct", "Correct! The area is 50 square units.", icon="info")
            else:
                messagebox.showerror("Incorrect", "Incorrect! Try again.", icon="error")
        except ValueError:
            messagebox.showerror("Invalid Input", "Please enter a valid number.", icon="error")

# Creating the main window
root = tk.Tk()
app = ITSApp(root)

# Running the application
root.mainloop()

