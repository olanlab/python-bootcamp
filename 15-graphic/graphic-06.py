import tkinter as tk

root = tk.Tk()

# Load the image file
image_file = "image.png"
image = tk.PhotoImage(file=image_file, )

image = image.subsample(3)

# Create a label to display the image
label = tk.Label(root, image=image )
label.pack()

# Run the Tkinter event loop
root.mainloop()
