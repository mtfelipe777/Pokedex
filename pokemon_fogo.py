from pokemon import Pokemon
class PokemonFogo(Pokemon):
    def imprimir_dados(self):
        return f"Pokemon de fogo: {self.nome}, Tipo: {self.tipo}, Nível: {self.nivel}, Capturado: {self.capturado}"