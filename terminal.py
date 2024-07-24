
launched = True
command = ""
terminal_name = "Default"

while launched:
    command = input(f"[{terminal_name}]> ")
    if command == "run":
        pass
    elif command == "chname":
        terminal_name = input("Nouveau nom du terminal : ")
    elif command == "help":
        print("""
\nLISTE DES COMMANDES DISPONIBLES :
---------------------------------
run    : Exécute ma fonction
chname : Change le nom du terminal
help   : Affiche l'aide sur les différentes commandes
quit   : Permet de quitter le terminal""")
    elif command == "quit":
        launched = False
    else:
        print("Commande introuvable")
