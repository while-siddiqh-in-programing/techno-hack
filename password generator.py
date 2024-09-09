import random
import string
from tkinter import *

def generate_password(length=16):
    try:
        length = int(length)
        if length < 4:
            lbl.config(text="Length too short!")
            return

        # Ensure at least one of each required character type
        password = [
            random.choice(string.ascii_uppercase),
            random.choice(string.ascii_lowercase),
            random.choice(string.digits),
            random.choice(string.punctuation)
        ]

        # Fill the rest of the password with random characters
        password += random.choices(string.ascii_letters + string.digits + string.punctuation, k=length-4)

        # Shuffle the list to randomize character positions
        random.shuffle(password)

        # Join the list into a string
        final_password = ''.join(password)

        # Update the label in the GUI with the generated password
        lbl.config(text=final_password)
    except ValueError:
        lbl.config(text="Invalid input! Enter a number.")

# Tkinter setup
root = Tk()
root.title("PASSWORD GENERATOR")
root.geometry("550x350")

# Entry to input password length
length_label = Label(root, text="Enter password length:", font=("Arial", 12))
length_label.grid(row=0, column=0, padx=10, pady=10)

length_entry = Entry(root, font=("Arial", 12))
length_entry.grid(row=0, column=1, padx=10, pady=10)

# Button to generate password
btn = Button(root, text="Generate Password", command=lambda: generate_password(length_entry.get()))
btn.grid(row=2, column=1, pady=20)

# Label to display the generated password
lbl = Label(root, font=("times", 15, "bold"))
lbl.grid(row=4, column=1, pady=20)

# Run the Tkinter loop
root.mainloop()
