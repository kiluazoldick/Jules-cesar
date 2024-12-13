import tkinter as tk
from tkinter import ttk

class MessagingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Jules Cesar ")

        # Style
        self.style = ttk.Style()
        self.style.configure("TFrame", background="#f0f0f0")
        self.style.configure("TButton", background="#007bff", foreground="black", font=("Helvetica", 12))

        # Création de la fenêtre principale
        self.frame = ttk.Frame(root)
        self.frame.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Bouton pour la création de compte
        self.create_account_button = ttk.Button(self.frame, text="Créer un compte", command=self.create_account)
        self.create_account_button.grid(row=0, column=0, padx=10, pady=10, sticky="nsew")

        # Bouton pour se connecter
        self.login_button = ttk.Button(self.frame, text="Se connecter", command=self.login)
        self.login_button.grid(row=0, column=1, padx=10, pady=10, sticky="nsew")

        # Configuration du poids des lignes et colonnes
        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)
        self.frame.grid_rowconfigure(0, weight=1)
        self.frame.grid_columnconfigure(0, weight=1)
        self.frame.grid_columnconfigure(1, weight=1)

    def create_account(self):
        # À faire : logique de création de compte
        create_account_window = tk.Toplevel(self.root)
        create_account_window.title("Créer un compte")
        # Ajoutez ici les widgets pour le formulaire de création de compte

    def login(self):
        # À faire : logique de connexion
        login_window = tk.Toplevel(self.root)
        login_window.title("Se connecter")
        # Ajoutez ici les widgets pour le formulaire de connexion

# Initialisation de l'application
if __name__ == "__main__":
    root = tk.Tk()
    app = MessagingApp(root)
    root.mainloop()
