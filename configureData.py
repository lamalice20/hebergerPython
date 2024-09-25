import os, json, time


with open('ServerConfig.json', "r") as ReadJsonConfig:
    data = json.load(ReadJsonConfig)

def change_host():
    host = input('Entrer la nouvelle adresse IP du server : ')
    data["hostIP"] = host

    with open('ServerConfig.json', "w") as WriteJsonConfig:
        try:
            json.dump(data, WriteJsonConfig, indent=4)
        except Exception as e:
            print(e)
        finally:
            WriteJsonConfig.close()

def change_port():
    port = int(input('Entrer le nouveau port du serveur : '))
    data["port"] = port

    with open('ServerConfig.json', "w") as WriteJsonConfig:
        try:
            json.dump(data, WriteJsonConfig, indent=4)
        except Exception as e:
            print(e)
        finally:
            WriteJsonConfig.close()

def change_path():
    path = input("Entrer le nouveau chemin d'accès vers le site : ")
    data["path"] = path


    with open('ServerConfig.json', "w") as WriteJsonConfig:
        try:
            json.dump(data, WriteJsonConfig, indent=4)
        except Exception as e:
            print(e)
        finally:
            WriteJsonConfig.close()

while True:
    choice = input("choice : \n1. Changer l'ip du site\n2. Changer le port du site\n3. Changer le chemain d'accès du site\n4. quitter\n\n\n")
    
    if choice == "1":
        change_host()
    
    if choice == "2":
        change_port()
    
    if choice == "3":
        change_path()
    
    if choice == "4":
        quit()