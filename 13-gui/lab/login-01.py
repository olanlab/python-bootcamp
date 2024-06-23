import tkinter as tk


# Create main window
root = tk.Tk()
root.title("Login")
customer_frame = tk.Frame(root)


def login():
    username = username_entry.get()
    password = password_entry.get()
    # Perform login validation here
    if username == "admin" and password == "password":
        root.title("Customer Record Application")
        login_frame.destroy()
        customer_frame.pack()
    else:
        error_label.config(text="Invalid username or password")

def add_customer():
    name = name_entry.get()
    phone = phone_entry.get()
    email = email_entry.get()
    # Perform customer record validation and saving here
    if name and phone and email:
        record_label.config(text=f"Added customer: {name}")
    else:
        record_label.config(text="Invalid customer record")



# Create login frame with username and password labels and entry fields
login_frame = tk.Frame(root)
username_label = tk.Label(login_frame, text="Username")
username_entry = tk.Entry(login_frame)
password_label = tk.Label(login_frame, text="Password")
password_entry = tk.Entry(login_frame, show="*")
login_label = tk.Label(login_frame, text="Please log in")
error_label = tk.Label(login_frame, fg="red")
login_button = tk.Button(login_frame, text="Login", command=login)

username_label.grid(row=0, column=0)
username_entry.grid(row=0, column=1)
password_label.grid(row=1, column=0)
password_entry.grid(row=1, column=1)
login_label.grid(row=2, column=0, columnspan=2)
error_label.grid(row=3, column=0, columnspan=2)
login_button.grid(row=4, column=0, columnspan=2)
login_frame.pack()


# Create customer frame with customer record entry fields and add button

name_label = tk.Label(customer_frame, text="Name")
name_entry = tk.Entry(customer_frame)
phone_label = tk.Label(customer_frame, text="Phone")
phone_entry = tk.Entry(customer_frame)
email_label = tk.Label(customer_frame, text="Email")
email_entry = tk.Entry(customer_frame)
add_button = tk.Button(customer_frame, text="Add Customer", command=add_customer)
record_label = tk.Label(customer_frame)

name_label.grid(row=0, column=0)
name_entry.grid(row=0, column=1)
phone_label.grid(row=1, column=0)
phone_entry.grid(row=1, column=1)
email_label.grid(row=2, column=0)
email_entry.grid(row=2, column=1)
add_button.grid(row=3, column=0, columnspan=2)
record_label.grid(row=4, column=0, columnspan=2)

# Hide customer frame initially
customer_frame.pack_forget()

# Start GUI
root.mainloop()
