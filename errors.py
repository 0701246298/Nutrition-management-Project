import tkinter as tk
from tkinter import messagebox


def login():
    username = entry_username.get()
    password = entry_password.get()

    if not username or not password:
        messagebox.showerror("Error", "Missing field. Please fill in both username and password.")
    elif username == "admin" and password == "1234":
        messagebox.showinfo("Success", "Login successful!")
        open_inner_interface()
    else:
        messagebox.showerror("Error", "Invalid input. Please check your username and password.")


def open_inner_interface():

    # Create the inner interface
    inner_root = tk.Tk()
    inner_root.title("Welcome Admin")

    # Set the window size
    inner_root.geometry("300x200")

    # Configure the inner interface
    inner_root.configure(bg="grey")  # Set background color

    # Display welcome message
    welcome_label = tk.Label(inner_root, text="Welcome Admin", font=("Helvetica", 16))
    welcome_label.pack(pady=50)

    # Start the inner loop
    inner_root.mainloop()


# Create the main window
root = tk.Tk()
root.title("Login Interface")

# Set the window size
root.geometry("300x200")

# Create and configure outer border frame
outer_frame = tk.Frame(root, bd=5, relief=tk.SOLID, bg='blue')
outer_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

# Create and configure inner border frame
inner_frame = tk.Frame(outer_frame, bd=5, relief=tk.SOLID,bg='green')
inner_frame.pack(padx=20, pady=10)

# Create labels and entry widgets for username and password
label_username = tk.Label(inner_frame, text="Username:")
label_username.grid(row=0, column=0, sticky=tk.W, pady=5)

entry_username = tk.Entry(inner_frame)
entry_username.grid(row=0, column=1, pady=5)

label_password = tk.Label(inner_frame, text="Password:")
label_password.grid(row=1, column=0, sticky=tk.W, pady=5)

entry_password = tk.Entry(inner_frame, show="*")
entry_password.grid(row=1, column=1, pady=5)

# Create login button
login_button = tk.Button(inner_frame, text="Login", command=login)
login_button.grid(row=2, columnspan=2, pady=10)

# Start the main loop
root.mainloop()
