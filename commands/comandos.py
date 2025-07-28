import json
import os

class tarefas:
    registros = "dados/ficha_player.json"

    def carregar_registros(self):
        if os.path.exists(self.registros):
            with open(self.registros, "r", encoding="utf-8") as f:
                return json.load(f)
            
        return []

    def salvar_dados(self, dados):
        with open(self.registros, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def nome_existe(self, registros, nome):
        for r in registros:
            if r["nome"].lower() == nome.lower():
                return True
            
        return False

    def info_registro(self, name, classe):
        return {
            name: {
                "classe": classe,
                "level": 0,
                "xp": 0,
                "fase": 1, #fase cria uma ponto de save, para o player abrir e ja ir para onde parou, vai precisar usar o decorador kkkkk
            },
        }

    def registrar_player(self, nome, classe):
        dados = self.carregar_registros()

        if nome in dados:
            print(f"{nome}, Ja existe um registro nesse com esse nome")
            return
        
        dados[nome] = self.info_registro(nome, classe)
        self.salvar_dados(dados)
        print(f"Bem vindo jogador, {nome}")

