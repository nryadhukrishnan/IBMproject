import tkinter as tk
from tkinter import messagebox, scrolledtext
import hashlib
import os
import sys
import time  # Import time module
from tkinter import ttk
import webbrowser
from tkinter import font as tkfont

# Create the root window first
root = tk.Tk()
root.withdraw()  # Hide the root window as it's not needed right now

# Constants for styling
DEFAULT_WORDLIST = 'wordlists/rockyou.txt'
FONT_LARGE = tkfont.Font(family="Helvetica", size=22, weight="bold")
FONT_MEDIUM = tkfont.Font(family="Helvetica", size=14)
FONT_SMALL = tkfont.Font(family="Helvetica", size=12)
BG_COLOR = '#1e1e1e'  # Dark gray background
HEADER_COLOR = '#00ff00'  # Bright green header
TEXT_COLOR = '#ffffff'  # White text
BUTTON_COLOR = '#28a745'  # Green button
BUTTON_HOVER_COLOR = '#218838'  # Darker green on hover
DISCL_COLOR = '#ff0000'  # Red for disclaimer text
FOOTER_COLOR = '#1a1a1a'  # Dark gray for footer

def start_crack():
    hash_type = hash_type_entry.get().upper()
    hash_value = hash_entry.get()

    if not hash_type or not hash_value:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    if not os.path.isfile(DEFAULT_WORDLIST):
        messagebox.showerror("Error", f"Wordlist file not found at {DEFAULT_WORDLIST}. Ensure the 'rockyou.txt' file is in the 'wordlists' folder.")
        return

    result_text.delete(1.0, tk.END)  # Clear previous results

    start_time = time.time()  # Start time

    try:
        with open(DEFAULT_WORDLIST, 'r', encoding="latin-1") as word_list_file:
            word_list = word_list_file.read().splitlines()

        for word in word_list:
            if hash_type == "MD5":
                hash_object = hashlib.md5(word.encode('utf-8'))
            elif hash_type == "SHA1":
                hash_object = hashlib.sha1(word.encode('utf-8'))
            elif hash_type == "SHA224":
                hash_object = hashlib.sha224(word.encode('utf-8'))
            elif hash_type == "SHA512":
                hash_object = hashlib.sha512(word.encode('utf-8'))
            elif hash_type == "SHA384":
                hash_object = hashlib.sha384(word.encode('utf-8'))
            else:
                messagebox.showerror("Error", "Invalid hash type. Please choose from the given options.")
                return

            hashed_word = hash_object.hexdigest()
            if hash_value == hashed_word:
                elapsed_time = time.time() - start_time  # Calculate elapsed time
                result_text.insert(tk.END, f"HASH FOUND: {word}\n")
                result_text.insert(tk.END, f"Time Taken: {elapsed_time:.2f} seconds\n")
                provide_feedback(word)  # Provide feedback on password strength
                break
        else:
            elapsed_time = time.time() - start_time  # Calculate elapsed time
            result_text.insert(tk.END, "HASH NOT FOUND\n")
            result_text.insert(tk.END, f"Time Taken: {elapsed_time:.2f} seconds\n")

    except FileNotFoundError:
        messagebox.showerror("Error", "Wordlist file not found. Please check the path and try again.")
    except Exception as e:
        messagebox.showerror("Error", f"An unexpected error occurred: {e}")

def provide_feedback(password):
    # Basic password strength feedback
    if len(password) < 8:
        feedback = "Password is too short. Consider using at least 8 characters."
    elif len(password) < 12:
        feedback = "Password length is acceptable but consider using more characters for better security."
    else:
        feedback = "Password length is good, but consider including a mix of uppercase, lowercase, numbers, and special characters."

    result_text.insert(tk.END, f"Password Strength Feedback:\n{feedback}\n")
    result_text.insert(tk.END, "Tips for a Strong Password:\n- Use at least 12 characters.\n- Include a mix of uppercase and lowercase letters.\n- Include numbers and special characters.\n- Avoid common words or easily guessable information.\n")

def clear_fields():
    hash_type_entry.delete(0, tk.END)
    hash_entry.delete(0, tk.END)
    result_text.delete(1.0, tk.END)

def show_main_app():
    global root
    root.deiconify()  # Show the root window

    root.title("Advanced Hash Cracker")
    root.geometry("1200x800")
    root.configure(bg=BG_COLOR)

    # Header
    header_frame = tk.Frame(root, bg=BG_COLOR)
    header_frame.pack(pady=10, fill=tk.X)

    header_label = tk.Label(header_frame, text="Advanced Hash Cracker", font=FONT_LARGE, bg=BG_COLOR, fg=HEADER_COLOR)
    header_label.pack()

    # Passwords Count
    password_count_label = tk.Label(root, text="The tool's password database contains over 14.3 million entries.", font=FONT_MEDIUM, bg=BG_COLOR, fg=TEXT_COLOR)
    password_count_label.pack(pady=10)

    # Instruction
    instruction_label = tk.Label(root, text="Enter the hash type and hash value to start cracking.", font=FONT_MEDIUM, bg=BG_COLOR, fg=TEXT_COLOR)
    instruction_label.pack(pady=10)

    # Hash Type Entry
    tk.Label(root, text="Hash Type (MD5, SHA1, SHA224, SHA512, SHA384):", font=FONT_MEDIUM, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    global hash_type_entry
    hash_type_entry = tk.Entry(root, width=80, font=FONT_SMALL, bg='#333333', fg=TEXT_COLOR, insertbackground='white')
    hash_type_entry.pack(pady=5)

    # Hash Value Entry
    tk.Label(root, text="Hash Value:", font=FONT_MEDIUM, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    global hash_entry
    hash_entry = tk.Entry(root, width=80, font=FONT_SMALL, bg='#333333', fg=TEXT_COLOR, insertbackground='white')
    hash_entry.pack(pady=5)

    # Buttons
    button_frame = tk.Frame(root, bg=BG_COLOR)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Start Cracking", command=start_crack, font=FONT_MEDIUM, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, relief=tk.FLAT).pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)
    tk.Button(button_frame, text="Clear", command=clear_fields, font=FONT_MEDIUM, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, relief=tk.FLAT).pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)

    # Results
    global result_text
    tk.Label(root, text="Results:", font=FONT_MEDIUM, bg=BG_COLOR, fg=TEXT_COLOR).pack(pady=5)
    result_text = scrolledtext.ScrolledText(root, width=80, height=15, wrap=tk.WORD, font=FONT_SMALL, bg='#333333', fg=TEXT_COLOR, insertbackground='white', relief=tk.FLAT)
    result_text.pack(pady=10)

    # Footer
    footer_frame = tk.Frame(root, bg=FOOTER_COLOR)
    footer_frame.pack(side=tk.BOTTOM, pady=10, fill=tk.X)

    # Footer Content
    footer_label = tk.Label(footer_frame, text=" © IBM_Project-HashedPasswordCracker. All rights reserved.", font=FONT_SMALL, bg=FOOTER_COLOR, fg=TEXT_COLOR, wraplength=1000, justify=tk.CENTER)
    footer_label.pack(side=tk.LEFT, padx=10)

    # Email Contact Button
    email_button = tk.Button(footer_frame, text="contact me", command=lambda: webbrowser.open("mailto:ttariyahgema@gmail.com"), font=FONT_SMALL, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, relief=tk.FLAT)
    email_button.pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=5)

    # Run the application
    root.mainloop()

def show_disclaimer():
    global disclaimer_window
    disclaimer_window = tk.Tk()
    disclaimer_window.title("Welcome")
    disclaimer_window.geometry("800x500")
    disclaimer_window.configure(bg=BG_COLOR)

   
    # Disclaimer Text
    disclaimer_text = tk.Label(disclaimer_window, text=" Hashed Password Cracker!\n\n"
                                                       "DISCLAIMER: This tool is intended for educational and ethical use only. By using this tool, you agree to comply with all applicable laws and regulations. Unauthorized access to systems or data is prohibited and punishable by law.We are not responsible for any misuse or illegal activity resulting from the use of this tool.Agree to continue.", 
                                                       font=FONT_MEDIUM, bg=BG_COLOR, fg=TEXT_COLOR, wraplength=750, justify=tk.LEFT)
    disclaimer_text.pack(pady=20)

    # Buttons
    button_frame = tk.Frame(disclaimer_window, bg=BG_COLOR)
    button_frame.pack(pady=20)

    tk.Button(button_frame, text="Agree and Continue", command=show_main_app, font=FONT_MEDIUM, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, relief=tk.FLAT).pack(side=tk.LEFT, padx=10, ipadx=10, ipady=5)
    tk.Button(button_frame, text="Exit", command=sys.exit, font=FONT_MEDIUM, bg=BUTTON_COLOR, fg=TEXT_COLOR, activebackground=BUTTON_HOVER_COLOR, relief=tk.FLAT).pack(side=tk.RIGHT, padx=10, ipadx=10, ipady=5)

    disclaimer_window.mainloop()

if __name__ == "__main__":
    show_disclaimer()
