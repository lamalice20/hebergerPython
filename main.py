import http.server as server
import socketserver as socket
import os
import json
import threading
import customtkinter as ctk
import tkinter as tk
from tkinter import messagebox, scrolledtext
import logging


# Charger la configuration depuis le fichier JSON
with open('ServerConfig.json', "r") as ReadJsonConfig:
    data = json.load(ReadJsonConfig)

host = data["hostIP"]
port = data["port"]
path = data["path"]  # Utiliser le chemin défini ou le répertoire courant si non spécifié
log_file_path = data["log_file"]
adress = (host, port)


# Configuration du logger pour afficher dans la console et enregistrer dans un fichier
logging.basicConfig(level=logging.INFO, format='%(message)s',
                    handlers=[logging.FileHandler(log_file_path),  # Fichier de log
                              logging.StreamHandler()])  # Console



# Custom HTTP Handler pour log des requêtes
class CustomRequestHandler(server.SimpleHTTPRequestHandler):
    def log_message(self, format, *args):
        # Log dans le fichier de log et la console
        log_entry = "%s - - [%s] %s\n" % (
            self.client_address[0],
            self.log_date_time_string(),
            format % args
        )
        logging.info(log_entry)  # Écrit à la fois dans le fichier et dans la console

        # Log dans l'interface
        app_text_log.insert(tk.END, log_entry)
        app_text_log.see(tk.END)  # Scroll automatiquement vers le bas

handler = CustomRequestHandler
httpd = socket.TCPServer(adress, handler)

# Démarrer le serveur dans un thread séparé pour ne pas bloquer l'interface
def start_server():
    global server_thread
    try:
        os.chdir(path)  # Changer le répertoire de travail vers le chemin spécifié
        server_thread = threading.Thread(target=httpd.serve_forever)
        server_thread.daemon = True
        server_thread.start()
        update_status(f"Le serveur tourne sur le port : {port}", "green")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Arrêter le serveur
def stop_server():
    try:
        httpd.shutdown()
        server_thread.join()
        update_status("Le serveur est arrêté !", "red")
    except Exception as e:
        messagebox.showerror("Erreur", str(e))

# Mettre à jour le statut du serveur dans l'interface
def update_status(status, color):
    label_status.configure(text=status, text_color=color)

# Création de la fenêtre principale
app = ctk.CTk()
app.title("Contrôle du Serveur HTTP")
app.geometry("600x450")

# Afficher l'adresse IP et le port actuels
label_host = ctk.CTkLabel(app, text=f"Adresse IP du serveur : {host}")
label_host.pack(pady=10)

label_port = ctk.CTkLabel(app, text=f"Port du serveur : {port}")
label_port.pack(pady=10)

# Afficher le chemin d'accès du serveur
if path == "./":
    label_path = ctk.CTkLabel(app, text=f"Chemin d'accès du serveur : {os.getcwd()}")
else:
    label_path = ctk.CTkLabel(app, text=f"Chemin d'accès du serveur : {path}")
label_path.pack(pady=10)

# Zone de texte pour afficher le statut du serveur
label_status = ctk.CTkLabel(app, text="Le serveur est arrêté", text_color="red")
label_status.pack(pady=20)

# Zone de texte déroulante pour afficher les logs des requêtes
app_text_log = scrolledtext.ScrolledText(app, width=70, height=10)
app_text_log.pack(pady=10)
app_text_log.insert(tk.END, "Logs des requêtes :\n")

# Ajouter des boutons pour démarrer et arrêter le serveur
button_start = ctk.CTkButton(app, text="Démarrer le serveur", command=start_server)
button_start.pack(pady=10)

button_stop = ctk.CTkButton(app, text="Arrêter le serveur", command=stop_server)
button_stop.pack(pady=10)

# Lancer l'interface graphique
app.mainloop()
