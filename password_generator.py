import customtkinter as ctk
import random
import string
import tkinter as tk
from tkinter import messagebox
import pyperclip

def generate_password(length, use_upper, use_lower, use_digits, use_special):
    chars = ''
    if use_upper:
        chars += string.ascii_uppercase
    if use_lower:
        chars += string.ascii_lowercase
    if use_digits:
        chars += string.digits
    if use_special:
        chars += string.punctuation
    
    if not chars:
        messagebox.showerror("Error", "Please select at least one character type")
        return ""
    
    return ''.join(random.choice(chars) for _ in range(length))

def on_generate():
    if length_entry.get() == "":
        messagebox.showerror("Error", "Please enter a password length")
        return
    length = int(length_entry.get())
    if length < 4 or length > 40:
        messagebox.showerror("Error", "Password length must be at least 4 characters and at most 50 characters")
        return
    use_upper = upper_var.get()
    use_lower = lower_var.get()
    use_digits = digits_var.get()
    use_special = special_var.get()
    
    length_entry.delete(0, tk.END)
    
    password = generate_password(length, use_upper, use_lower, use_digits, use_special)
    password_entry.delete(0, tk.END)
    password_entry.insert(0, password)
    

def copy_to_clipboard():
    if password_entry.get() == "":
        messagebox.showerror("Error", "No password to copy")
        return
    pyperclip.copy(password_entry.get())
    messagebox.showinfo("Info", "Password copied to clipboard")
    password_entry.delete(0, tk.END)
    
height=500
width=600
app = ctk.CTk()
app.geometry(f"{width}x{height}")
app.title("Password Generator")
app.resizable(0,0)
app.grid_columnconfigure(0, weight=80)
app.grid_columnconfigure(1, weight=10)
app.grid_rowconfigure(0, weight=10)
app.grid_rowconfigure(1, weight=80)



length_entry = ctk.CTkEntry(app,
                            height=20,
                            placeholder_text="Enter Password Length",
                            placeholder_text_color="gray",
                            bg_color="black",
                            fg_color="white",
                            corner_radius=10, 
                            text_color="black",
                            border_width=2,
                            border_color="white",
                            font=("JetBrainsMono", 18))
length_entry.grid(row=0, column=0, padx=5, pady=10,sticky='nwes')

generate_button = ctk.CTkButton(app,
                                height=20,
                                bg_color="black",
                                fg_color="white",
                                corner_radius=10,
                                text_color="black",
                                border_width=2,
                                border_color="white",
                                hover_color="lightgray",
                                font=("JetBrainsMono", 18),
                                text="Generate Password", 
                                command=on_generate)
generate_button.grid(row=0, column=1, padx=5, pady=10,sticky='news')


master_frame = ctk.CTkFrame(app,
                            width=width-20,
                            border_width=2,
                            corner_radius=10,
                            border_color="white",
                            bg_color="black",
                            fg_color="white")
master_frame.grid(row=1, column=0, padx=5, pady=5,sticky='nswe',columnspan=2)
master_frame.grid_columnconfigure(0, weight=80)
master_frame.grid_columnconfigure(1, weight=1)
master_frame.grid_rowconfigure(0, weight=50)
master_frame.grid_rowconfigure(1, weight=5)

upper_var = tk.BooleanVar()
lower_var = tk.BooleanVar()
digits_var = tk.BooleanVar()
special_var = tk.BooleanVar()

options_frame = ctk.CTkFrame(master_frame,
                                bg_color="white",
                                fg_color="white",
                                corner_radius=10,
                                border_width=2,
                                border_color="black")
options_frame.grid(row=0, column=0, padx=10, pady=10,sticky='nswe',columnspan=2)

upper_check = ctk.CTkCheckBox(options_frame, 
                              text="Include Uppercase",
                              text_color="black",
                              bg_color="white",
                              fg_color="white",
                                font=("JetBrainsMono", 18),
                                corner_radius=5,
                                border_width=2,
                                border_color="black",
                                checkmark_color="black",
                                hover_color="lightgray", 
                              variable=upper_var)
upper_check.grid(row=0, column=0, columnspan=2, padx=10,ipadx=5, pady=5,ipady=5,sticky='nswe')

lower_check = ctk.CTkCheckBox(options_frame,
                              text="Include Lowercase",
                              text_color="black",
                              bg_color="white",
                              fg_color="white",
                                font=("JetBrainsMono", 18),
                                corner_radius=5,
                                border_width=2,
                                border_color="black",
                                checkmark_color="black",
                                hover_color="lightgray", 
                              variable=lower_var)
lower_check.grid(row=1, column=0, columnspan=2, padx=10,ipadx=5, pady=5,ipady=5,sticky='nsew')

digits_check = ctk.CTkCheckBox(options_frame, 
                               text="Include Digits",
                               text_color="black",
                               bg_color="white",
                              fg_color="white",
                                font=("JetBrainsMono", 18),
                                corner_radius=5,
                                border_width=2,
                                border_color="black",
                                checkmark_color="black",
                                hover_color="lightgray", 
                               variable=digits_var)
digits_check.grid(row=2, column=0, columnspan=2, padx=10,ipadx=5, pady=5,ipady=5,sticky='nsew')

special_check = ctk.CTkCheckBox(options_frame, 
                                text="Include Special Characters",
                                text_color="black",
                                bg_color="white",
                              fg_color="white",
                                font=("JetBrainsMono", 18),
                                corner_radius=5,
                                border_width=2,
                                border_color="black",
                                checkmark_color="black",
                                hover_color="lightgray",
                                variable=special_var)
special_check.grid(row=3, column=0, columnspan=2, padx=10,ipadx=5, pady=5,ipady=5,sticky='nsew')

password_entry = ctk.CTkEntry(master_frame,
                              text_color="black", 
                              height=30,
                              bg_color="white",
                              fg_color="white",
                              placeholder_text= "Generated Password",
                              placeholder_text_color="grey",
                              border_width=2,
                              border_color="black",
                              corner_radius=10,
                              font=("JetBrainsMono", 18))
password_entry.grid(row=4, column=0, padx=10, pady=5,sticky='nsew')


copy_button = ctk.CTkButton(master_frame,
                                    text="Copy to Clipboard",
                                    text_color="black",
                                    fg_color="white",
                                    bg_color="white",
                                    font=("JetBrainsMono", 18),
                                    border_width=2,
                                    border_color="black",
                                    hover_color="lightgray",
                                    
                                    corner_radius=10,
                                    command=lambda: copy_to_clipboard())
copy_button.grid(row=4, column=1, padx=10, pady=5,sticky='nwse')

app.mainloop()
