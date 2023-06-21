import tkinter as tk

# Create the Tkinter window
root = tk.Tk()

# Load the image file
image_file = "image.png"
image = tk.PhotoImage(file=image_file)

image = image.subsample(4)

canvas = tk.Canvas(root, width=image.width(), height=image.height())
canvas.pack()

# Add the image to the canvas
canvas.create_image(image.width()/2, image.height()/2, image=image)

# Run the Tkinter event loop
root.mainloop()