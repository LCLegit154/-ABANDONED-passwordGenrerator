import tkinter as tk
import random
import string

# Function to generate a random password
def generate_password():
    length = 20  # Change this to set the length of the password
    characters = string.ascii_letters + string.digits
    password = ''.join(random.choice(characters) for _ in range(length))
    
    password_entry.config(state="normal")  # Set the entry to normal state
    password_entry.delete(0, tk.END)  # Clear previous content
    password_entry.insert(0, password)  # Insert new password
    password_entry.config(state="readonly")  # Set the entry back to readonly state

# Function to exit the application
def exit_app():
    app.destroy()

# Create the main application window
app = tk.Tk()
app.title("Random Password Generator")

# Set the background color of the main window
app.configure(bg="black")

# Set the width and height of the window
window_width = 400
window_height = 300  # Increased height to accommodate the exit button
screen_width = app.winfo_screenwidth()
screen_height = app.winfo_screenheight()
x_coordinate = (screen_width - window_width) // 2
y_coordinate = (screen_height - window_height) // 2
app.geometry(f"{window_width}x{window_height}+{x_coordinate}+{y_coordinate}")

# Create a custom font for the button text
button_font = ("Helvetica", 14, "bold")

# Create widgets
generate_button = tk.Button(app, text="Generate password", command=generate_password, bg="black", fg="black",
                            font=button_font, bd=4, relief="raised")
password_entry = tk.Entry(app, state="readonly", bg="black", fg="white", font=("Helvetica", 12))
exit_button = tk.Button(app, text="Exit", command=exit_app, bg="black", fg="black",
                        font=button_font, bd=4, relief="raised")

# Organize widgets using the grid layout
generate_button.pack(pady=(20, 10))
password_entry.pack(pady=5)
exit_button.pack(pady=(10, 20))

# Start the main event loop
app.mainloop()
