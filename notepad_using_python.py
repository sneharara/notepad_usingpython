import tkinter as tk
from tkinter import filedialog, messagebox

# Function to open a file
def open_file():
    filepath = filedialog.askopenfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        try:
            with open(filepath, "r") as file:
                text_area.delete(1.0, tk.END)  # Clear existing content
                text_area.insert(tk.END, file.read())  # Insert file content
        except Exception as e:
            messagebox.showerror("Error", f"Failed to open file: {e}")

# Function to save a file
def save_file():
    filepath = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt"), ("All files", "*.*")])
    if filepath:
        try:
            with open(filepath, "w") as file:
                file.write(text_area.get(1.0, tk.END))  # Save content
        except Exception as e:
            messagebox.showerror("Error", f"Failed to save file: {e}")

# Function to handle exit
def on_exit():
    if messagebox.askokcancel("Quit", "Do you want to quit?"):
        root.quit()

# Create the main window
root = tk.Tk()
root.title("Simple Notepad")
root.geometry("600x400")

# Create a text area widget
text_area = tk.Text(root, wrap=tk.WORD, font=("Arial", 12))
text_area.pack(expand=True, fill=tk.BOTH)

# Create a menu bar
menu_bar = tk.Menu(root)

# Create the File menu
file_menu = tk.Menu(menu_bar, tearoff=0)
file_menu.add_command(label="Open", command=open_file)
file_menu.add_command(label="Save", command=save_file)
file_menu.add_separator()
file_menu.add_command(label="Exit", command=on_exit)
menu_bar.add_cascade(label="File", menu=file_menu)

# Attach the menu to the root window
root.config(menu=menu_bar)

# Run the Tkinter event loop
root.mainloop()
