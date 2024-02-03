import tkinter as tk
from tkinter import messagebox
import pickle

class SalaryPredictionApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Salary Prediction")

        
        # Load the ML model using Pickle
        with open("finalized_model.pkl", 'rb') as model_file: # Replace with your actual model file path
            self.model = pickle.load(model_file)


        # Create and pack widgets
        self.label_name = tk.Label(root, text="Name:")
        self.label_name.pack(pady=10)
        self.entry_name = tk.Entry(root)
        self.entry_name.pack(pady=10)

        self.label_yearExperience = tk.Label(root, text="Years of Experience:")
        self.label_yearExperience.pack(pady=10)
        self.entry_yearExperience = tk.Entry(root)
        self.entry_yearExperience.pack(pady=10)


        self.button_predict_salary = tk.Button(root, text="Predict", command=self.predict_salary)
        self.button_predict_salary.pack(pady=20)


    def predict_salary(self):
        try:
            # Get user inputs
            name = self.entry_name.get()
            yearExperience = float(self.entry_yearExperience.get())

            # Example: Use the loaded ML model for prediction
            features = [[yearExperience]]
            prediction = self.model.predict(features)[0]

            # Display result based on prediction
            messagebox.showinfo("Salary Prediction", f"Hey, {name}! Your salary should be ${prediction:.2f}")

        except ValueError:
            messagebox.showerror("Error", "Please enter valid numerical values for Years of Experience.")


root = tk.Tk()
app = SalaryPredictionApp(root)
root.mainloop()
