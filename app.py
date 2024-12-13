import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from ttkthemes import ThemedStyle

def caesar_cipher(message, shift):
    encrypted_message = ""
    for char in message:
        if char.isalpha():  
            shifted_char = chr((ord(char) - 65 + shift) % 26 + 65) if char.isupper() else chr((ord(char) - 97 + shift) % 26 + 97)
            encrypted_message += shifted_char
        else:
            encrypted_message += char  
    return encrypted_message

def encode_message():
    message = entry_message.get()
    shift = int(combo_shift.get())
    encrypted_message = caesar_cipher(message, shift)
    text_encrypted.delete('1.0', tk.END)  
    text_encrypted.insert(tk.END, "Message codé : " + encrypted_message)

def send_message():
    message = text_encrypted.get('1.0', tk.END)
    messagebox.showinfo("Message envoyé", f"Le message a été envoyé : {message}")

# Création de la fenêtre principale
root = tk.Tk()
root.title("Encodeur César - WhatsApp Style")

# Appliquer le thème
style = ThemedStyle(root)
style.set_theme("equilux")  # Choix du thème "equilux" (style sombre)

# Création des widgets
label_message = ttk.Label(root, text="Message à coder:", style="Dark.TLabel")
label_message.grid(row=0, column=0, padx=10, pady=5, sticky='nsew')

entry_message = ttk.Entry(root)
entry_message.grid(row=0, column=1, padx=10, pady=5, sticky='nsew')

label_shift = ttk.Label(root, text="Indice de codage:", style="Dark.TLabel")
label_shift.grid(row=1, column=0, padx=10, pady=5, sticky='nsew')

combo_shift = ttk.Combobox(root, values=list(range(1, 26)), style="Dark.TCombobox")
combo_shift.current(0)
combo_shift.grid(row=1, column=1, padx=10, pady=5, sticky='nsew')

button_encode = ttk.Button(root, text="Coder", command=encode_message, style="Dark.TButton")
button_encode.grid(row=2, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

text_encrypted = tk.Text(root, height=4, bg="#202124", fg="#ffffff", insertbackground="#ffffff")
text_encrypted.grid(row=3, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

button_send = ttk.Button(root, text="Envoyer", command=send_message, style="Dark.TButton")
button_send.grid(row=4, column=0, columnspan=2, padx=10, pady=5, sticky='nsew')

# Configuration du poids des lignes et colonnes pour permettre l'expansion
root.grid_rowconfigure(0, weight=1)
root.grid_rowconfigure(1, weight=1)
root.grid_rowconfigure(2, weight=1)
root.grid_rowconfigure(3, weight=1)
root.grid_rowconfigure(4, weight=1)
root.grid_columnconfigure(0, weight=1)
root.grid_columnconfigure(1, weight=1)

# Lancement de la boucle principale
root.mainloop()
