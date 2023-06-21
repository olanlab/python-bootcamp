import tkinter as tk
import sys
import os



root = tk.Tk()


if getattr(sys, 'frozen', False):
     extDataDir = sys._MEIPASS
     extDataDir  = os.path.join(extDataDir, 'assets/images/image.png')      
else:
     extDataDir = os.getcwd()
     extDataDir = os.path.join(extDataDir, 'assets/images/image.png') 
print(f"path of extDataDir is {extDataDir}")

# Load the image file
image = tk.PhotoImage(file=extDataDir, )

image = image.subsample(3)

# Create a label to display the image
label = tk.Label(root, image=image )
label.pack()

# Run the Tkinter event loop
root.mainloop()
