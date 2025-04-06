import base64
import tkinter as tk

def encrypt(file1):
    with open(file1, "r+") as file:
        content = file.read()
        with open(file1, "w") as file:
            file.write(base64.b64encode(content.encode("utf-8")).decode("utf-8"))

def decode(file1):
    with open(file1, "r") as file:
        content = file.read()
        with open(file1, "w") as file:
            file.write(base64.b64decode(content.encode("utf-8")).decode("utf-8"))

"""Window Configuration"""
root = tk.Tk()
root.geometry("500x500")
root.title("Encrypting")
root.config(bg = "#454545")

"""UI Elements"""
label = tk.Label(root, text = "Enter the file name:", font = ("Arial", 12), bg = "#454545", fg = "#ffffff")
label.pack()
entry = tk.Entry(root, width = 25, font = ("Arial", 12), bg = "#454545", fg = "#ffffff")
entry.pack()
entry.place(relx = 0.5, rely = 0.2, anchor = "center")
encrypt_button = tk.Button(root, text = "Encrypt", command = lambda: encrypt(entry.get()), font = ("Arial", 12), bg = "#656565", fg = "#ffffff")
encrypt_button.pack()
encrypt_button.place(relx = 0.5, rely = 0.4, anchor = "center")
decode_button = tk.Button(root, text = "Decode", command = lambda: decode(entry.get()), font = ("Arial", 12), bg = "#656565", fg = "#ffffff")
decode_button.pack()
decode_button.place(relx = 0.5, rely = 0.6, anchor = "center")

tk.mainloop()