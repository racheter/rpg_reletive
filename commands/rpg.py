from commands.comandos import tarefas


class play(tarefas):

    def register(self):
        print("=+= Escolha seu nome =+=")
        nome_player = str(input("Nome: "))
        verificar = self.nome_existe(nome_player)

        if verificar == False:

            print("=+= Escolha sua classe =+=")
            classe_player = str(input("Classe: "))

            self.registrar_player(nome_player, classe_player)

        else: print(f"{nome_player}, Ja existe um registro nesse com esse nome")
