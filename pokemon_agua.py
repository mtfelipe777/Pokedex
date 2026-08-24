from pokemon import Pokemon
class PokemonAgua(Pokemon):
    
    def imprimir_dados(self):
        return f"Pokémon de água: {self.nome}, Tipo: {self.tipo}, Nível: {self.nivel}, Capturado: {self.capturado}."