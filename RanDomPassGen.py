import tkinter as tk
import secrets
import string
import tkinter.messagebox as messagebox

def generate_password():
    length = 16
    characters = string.ascii_letters + string.digits
    password = ''.join(secrets.choice(characters) for _ in range(length))
    
    password_entry.config(state="normal")
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    password_entry.config(state="readonly")

# Function to copy the password to clipboard
def copy_password():
    app.clipboard_clear()  # Clear any existing clipboard content
    password = password_entry.get()  # Get the content of the password_entry
    app.clipboard_append(password)  # Append the password to clipboard
    app.update()  # Update the clipboard content

# Function to remove the password from the clipboard
def remove_password_from_clipboard():
    app.clipboard_clear()  # Clear the clipboard content
    app.clipboard_append("")  # Append an empty string to effectively clear the clipboard
    app.update()  # Update the clipboard content


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
window_height = 400  # Increased height to accommodate the new button
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
copy_button = tk.Button(app, text="Copy Password", command=copy_password, bg="black", fg="black",
                        font=button_font, bd=4, relief="raised")
remove_button = tk.Button(app, text="Remove Pass from Clipboard", command=remove_password_from_clipboard, bg="black", fg="black",
                        font=button_font, bd=4, relief="raised")
exit_button = tk.Button(app, text="Exit", command=exit_app, bg="black", fg="black",
                        font=button_font, bd=4, relief="raised")

# Organize widgets using the grid layout
generate_button.pack(pady=(20, 10))
password_entry.pack(pady=5)
copy_button.pack(pady=5)
remove_button.pack(pady=5)
exit_button.pack(pady=(10, 20))

# Start the main event loop
app.mainloop()
