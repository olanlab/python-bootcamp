import tkinter as tk
import os

root = tk.Tk()

dirname, filename  = os.path.split(os.path.abspath(__file__))



# Load the image file
image_file = "image.png"
image = tk.PhotoImage(file=f'{dirname}/{image_file}', )

image = image.subsample(3)

# Create a label to display the image
label = tk.Label(root, image=image )
label.pack()

# Run the Tkinter event loop
root.mainloop()
