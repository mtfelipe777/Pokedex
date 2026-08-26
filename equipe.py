class Equipe:
    def __init__(self):
        self.pokemons = []

    def adicionar_pokemon(self, pokemon):
        if len(self.pokemons) < 3:
            self.pokemons.append(pokemon.nome)
            return True

        return False

    def remover_pokemon(self, nome):
        if nome in self.pokemons:
            self.pokemons.remove(nome)
            return True

        return False

    def listar_pokemons(self):
        return self.pokemons