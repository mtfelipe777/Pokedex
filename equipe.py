class Equipe:
    def __init__(self):
        self.pokemons = []
    def adicionar_pokemon(self, pokemon):
        if len(self.pokemons) < 3:
            self.pokemons.append(pokemon.nome)
            return True
        return False
    def remover_pokemon(self, nome):
        for pokemon in self.pokemons:
            if pokemon.nome == nome:
                self.pokemons.remove(pokemon)
                return True
        return False
    def listar_pokemons(self):
        for pokemon in self.pokemons:
            return self.pokemons
        