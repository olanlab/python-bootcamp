from tkinter import *

window = Tk()
window.title("Miles to Kilometers Converter")
window.config(padx=10, pady=10)

# Entry 
entry_miles = Entry(width=20, justify="right")
entry_miles.insert(END, string="20")
entry_miles.grid(column=1, row=0)

# Label
label_miles = Label(text="is equal to")
label_miles.grid(column=3, row=0)

label_miles = Label(text="Miles")
label_miles.grid(column=2, row=0)

label_output_kilometers = Label(text=f"".rjust(25, ' '), width=20)
label_output_kilometers.grid(column=4, row=0, sticky="E")

label_kilometers = Label(text="Km.")
label_kilometers.grid(column=5, row=0)

def miles_to_km() :
    try:
        miles = float(entry_miles.get())
        km = miles * 1.609
        label_output_kilometers.config(text=f"{round(km, 2)}".rjust(20, " "))
    except(Exception):
        label_output_kilometers.config(text=f"-".rjust(20, " "))



convert_btn = Button(text="Convert", width=20, command=miles_to_km)
convert_btn.grid(column=1,row=1, columnspan=2 )

def reset() :
    entry_miles.delete(0, END)
    entry_miles.insert(END, string="20")
    label_output_kilometers.config(text=f"".rjust(25, ' '))

reset_btn = Button(text="Reset", width=20, command=reset)
reset_btn.grid(column=3,row=1, columnspan=2 )

window.mainloop()