import tkinter as tk

# Create a new window
window = tk.Tk()

# Set the size of the window
window.geometry("400x200")

# Set the background color of the window
window.configure(bg='#2c3e50')

# Create a label and add it to the window
label = tk.Label(window, text="Welcome to my program!", font=('Arial', 18, 'bold'), fg='white', bg='#2c3e50')
label.grid(row=0, column=0, columnspan=2, pady=20)

# Create a text box and add it to the window
textbox = tk.Entry(window, font=('Arial', 14))
textbox.grid(row=1, column=0, padx=20, pady=10)

# Create a function to greet the user
def greet_user():
    name = textbox.get()
    if name:
        message = f"Hello, {name}! Welcome to my program!"
    else:
        message = "Please enter your name."
    greeting_label.config(text=message)

# Bind the <Return> event to the textbox widget
textbox.bind("<Return>", lambda event: greet_user())

# Create a button to submit the user's name
submit_button = tk.Button(window, text="Submit", bg='#3498db', fg='white', font=('Arial', 14, 'bold'), padx=20, pady=10, command=greet_user)
submit_button.grid(row=1, column=1)

# Create a label to display the greeting
greeting_label = tk.Label(window, font=('Arial', 14), fg='white', bg='#2c3e50')
greeting_label.grid(row=2, column=0, columnspan=2, pady=20)

# Start the main event loop
window.mainloop()
