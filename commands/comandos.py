import json
import os

class tarefas:
    registros = "dados/ficha_player.json"

    def carregar_registros(self):
        if os.path.exists(self.registros):
            with open(self.registros, "r", encoding="utf-8") as f:
                return json.load(f)      
        return []
    dados = carregar_registros

    def salvar_dados(self, dados):
        with open(self.registros, "w", encoding="utf-8") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)

    def nome_existe(self, nome):
        if nome in self.dados():
                return True
            
        else: return False

    def info_registro(self, classe):
        return {
            "classe": classe,
            "level": 0,
            "xp": 0,
            "vida": 100,
            "fase": 1, #fase cria uma ponto de save, para o player abrir e ja ir para onde parou, vai precisar usar o decorador kkkkk
            }

    def registrar_player(self, nome, classe):
        dados = self.dados()
        dados[nome] = self.info_registro(classe)
        self.salvar_dados(dados)

        print(f"Bem vindo jogador, {nome}")

