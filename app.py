import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import os

def select_images():
    filetypes = (
        ('Image files', '*.jpeg *.jpg *.png'),
        ('All files', '*.*')
    )
    filenames = filedialog.askopenfilenames(title='Select images', initialdir='/', filetypes=filetypes)
    listbox.delete(0, tk.END)  # Clear existing listbox entries
    for filename in filenames:
        listbox.insert(tk.END, filename)
    images_list.extend(filenames)

def convert_to_pdf():
    if not images_list:
        messagebox.showerror("Error", "No images selected!")
        return

    save_path = filedialog.asksaveasfilename(defaultextension='.pdf', filetypes=[("PDF files", '*.pdf')])
    if not save_path:
        return

    try:
        image_objects = [Image.open(x).convert('RGB') for x in images_list]
        image_objects[0].save(save_path, save_all=True, append_images=image_objects[1:])
        messagebox.showinfo("Success", f"PDF saved successfully at {save_path}")
    except Exception as e:
        messagebox.showerror("Error", f"Failed to convert to PDF: {e}")

def clear_list():
    listbox.delete(0, tk.END)
    images_list.clear()

# GUI setup
root = tk.Tk()
root.title('Image to PDF Converter')
root.geometry('600x400')

images_list = []

# Frame for Listbox and Scrollbar
frame = tk.Frame(root)
frame.pack(pady=20)

listbox = tk.Listbox(frame, width=50, height=10)
listbox.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

scrollbar = tk.Scrollbar(frame, orient=tk.VERTICAL, command=listbox.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

listbox.config(yscrollcommand=scrollbar.set)

# Buttons
button_frame = tk.Frame(root)
button_frame.pack(pady=20)

select_button = tk.Button(button_frame, text="Select Images", command=select_images)
select_button.pack(side=tk.LEFT, padx=10)

convert_button = tk.Button(button_frame, text="Convert to PDF", command=convert_to_pdf)
convert_button.pack(side=tk.LEFT, padx=10)

clear_button = tk.Button(button_frame, text="Clear List", command=clear_list)
clear_button.pack(side=tk.LEFT, padx=10)

root.mainloop()
