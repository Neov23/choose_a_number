import random
import tkinter as tk

# Integer variable that will store the random number
choice = 0

def generate_randint(first, last):
    """
    Generate a random number between first and second parameter and update
    the label
    """
    global choice
    choice = random.randint(int(first), int(last))
    output_label.config(text=choice)

    # Changing label's position based on amount of digits, due to appearance
    if choice >= 0 and choice < 1_000:
        output_label.place(x=180, y=200)
    elif choice >= 1000 and choice < 1_000_000:
        output_label.place(x=160, y=200)
    elif choice >= 1_000_000:
        output_label.place(x=140, y=200)

# Initialize window attributes
root = tk.Tk()
root.title("Choose a number! (by Charitakis Dimitris)")
root.geometry("390x293+840+450")
root.resizable(False, False)
root.configure(bg='black')
root.iconbitmap("images/23.ico")

# Label related to first input number
label_first = tk.Label(root, text="From", bg="black", fg="green")
label_first.place(x=110, y=20)

# Entry for user to input his first desired number
entry_first = tk.StringVar()
entry_first = tk.Entry(root, textvariable=entry_first, bg="black", fg="green",
                bd=0)
entry_first.config(highlightbackground="green", highlightcolor="green",
                highlightthickness=1, insertbackground="green")
entry_first.place(x=150, y=20)
entry_first.focus()

# Label related to second input number
label_last = tk.Label(root, text="To", bg="black", fg="green")
label_last.place(x=122, y=60)

# Entry for user to input his second desired number
entry_last = tk.StringVar()
entry_last = tk.Entry(root, textvariable=entry_last, bg="black", fg="green",
                bd=0)
entry_last.config(highlightbackground="green", highlightcolor="green", 
                highlightthickness=1, insertbackground="green")
entry_last.place(x=150, y=60)

# Create button that generates random number between first and second entry
text = "Generate Random Number"
button_generator = tk.Button(root, text=text, width=30, height=3, bg="green",
            fg="black", command=lambda: generate_randint(entry_first.get(),
            entry_last.get()))
button_generator.place(x=90, y=110)

# Display random number
output_label = tk.Label(root, text=choice, bg="black", fg="green",
                font=("Arial", 25))

root.mainloop()