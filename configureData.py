import os
import json
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox

# Charger la configuration depuis le fichier JSON
with open('ServerConfig.json', "r") as ReadJsonConfig:
    data = json.load(ReadJsonConfig)

# Fonctions de mise à jour des paramètres
def change_host():
    host = entry_host.get()
    data["hostIP"] = host
    with open('ServerConfig.json', "w") as WriteJsonConfig:
        try:
            json.dump(data, WriteJsonConfig, indent=4)
            messagebox.showinfo("Succès", "L'adresse IP a été mise à jour.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

def change_port():
    try:
        port = int(entry_port.get())
        data["port"] = port
        with open('ServerConfig.json', "w") as WriteJsonConfig:
            try:
                json.dump(data, WriteJsonConfig, indent=4)
                messagebox.showinfo("Succès", "Le port a été mis à jour.")
            except Exception as e:
                messagebox.showerror("Erreur", str(e))
    except ValueError:
        messagebox.showerror("Erreur", "Veuillez entrer un port valide (nombre).")

def change_path():
    path = entry_path.get()
    data["path"] = path
    with open('ServerConfig.json', "w") as WriteJsonConfig:
        try:
            json.dump(data, WriteJsonConfig, indent=4)
            messagebox.showinfo("Succès", "Le chemin a été mis à jour.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

def change_log_file():
    log_file = entry_log_file.get()
    data["log_file"] = log_file
    with open('ServerConfig.json', "w") as WriteJsonConfig:
        try:
            json.dump(data, WriteJsonConfig, indent=4)
            messagebox.showinfo("Succès", "Le fichier de log a été mis à jour.")
        except Exception as e:
            messagebox.showerror("Erreur", str(e))

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Configuration du Serveur")
app.geometry("500x600")

# Ajouter des labels et des entrées pour chaque paramètre
label_host = ctk.CTkLabel(app, text="Nouvelle adresse IP :")
label_host.pack(pady=10)
entry_host = ctk.CTkEntry(app, width=200)
entry_host.pack(pady=5)

label_port = ctk.CTkLabel(app, text="Nouveau port :")
label_port.pack(pady=10)
entry_port = ctk.CTkEntry(app, width=200)
entry_port.pack(pady=5)

label_path = ctk.CTkLabel(app, text="Nouveau chemin d'accès :")
label_path.pack(pady=10)
entry_path = ctk.CTkEntry(app, width=200)
entry_path.pack(pady=5)

label_log_file = ctk.CTkLabel(app, text="Nouveau fichier de log :")
label_log_file.pack(pady=10)
entry_log_file = ctk.CTkEntry(app, width=200)
entry_log_file.pack(pady=5)

# Ajouter des boutons pour chaque action
button_host = ctk.CTkButton(app, text="Changer IP", command=change_host)
button_host.pack(pady=10)

button_port = ctk.CTkButton(app, text="Changer Port", command=change_port)
button_port.pack(pady=10)

button_path = ctk.CTkButton(app, text="Changer Chemin", command=change_path)
button_path.pack(pady=10)

button_log_file = ctk.CTkButton(app, text="Changer Fichier de Log", command=change_log_file)
button_log_file.pack(pady=10)

# Lancer l'interface graphique
app.mainloop()
