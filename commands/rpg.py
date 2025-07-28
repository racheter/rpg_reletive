from commands.comandos import tarefas

comandos = tarefas()

class play:
    def register(self):

        print("=+= Escolha sua classe =+=")
        classe_player = str(input("Classe: "))
        print("=+= Escolha seu nome =+=")
        nome_player = str(input("Nome: "))

        comandos.registrar_player(nome_player, classe_player)
