import ctypes
import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("BMI Calculator")

root.resizable(width=False, height=False)


# Create the labels and entry boxes for height and weight
height_label = tk.Label(root, text="Height (cm):")
height_label.grid(row=0, column=0, padx=10, pady=10)
height_entry = tk.Entry(root)
height_entry.grid(row=0, column=1, padx=10, pady=10)

weight_label = tk.Label(root, text="Weight (kg):")
weight_label.grid(row=1, column=0, padx=10, pady=10)
weight_entry = tk.Entry(root)
weight_entry.grid(row=1, column=1, padx=10, pady=10)

result_label = tk.Label(root, text="")
result_label.grid(row=3, columnspan=2)

# Create the function to calculate BMI
def calculate_bmi():
    height = float(height_entry.get()) / 100 # Convert height to meters
    weight = float(weight_entry.get())
    bmi = weight / (height ** 2)
    result_label.config(text="Your BMI is: {:.2f}".format(bmi))

# Create the calculate button
calculate_button = tk.Button(root, text="Calculate", command=calculate_bmi)
calculate_button.grid(row=2, columnspan=2, padx=10, pady=10)

# Run the main loop
root.mainloop()
