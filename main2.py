from pokemon_agua import PokemonAgua
from pokemon_fogo import PokemonFogo
from pokemon import Pokemon
from pokedex import Pokedex
from treinador import Treinador


pokedex = Pokedex()

nome_treinador = input("Digite o nome do treinador: ")
treinador = Treinador(nome_treinador)

while True:
    print("POKÉDEX:")
    print("1 - Cadastrar Pokémon")
    print("2 - Listar todos os Pokémons")
    print("3 - Listar Pokémons de água")
    print("4 - Listar Pokémons de fogo")
    print("5 - Ver Pokémon capturados")
    print("0 - Sair")

    opcao = input("Digite uma opção: ")

    if opcao == "1":
        print("CADASTRAR POKÉMON")

        nome = input("Nome do Pokémon: ")
        tipo = input("Tipo do Pokémon: ")
        nivel = int(input("Nível do Pokémon: "))
        capturado = input("O Pokémon foi capturado? (s/n): ")
        if tipo == "Água":
            pokemon = PokemonAgua(nome, tipo, nivel, capturado)
        elif tipo == "Fogo":
            pokemon = PokemonFogo(nome, tipo, nivel, capturado)
        else:
            pokemon = Pokemon(nome, tipo, nivel, capturado)

        pokedex.adicionar_pokemon(pokemon)

        if capturado == "Sim":
            treinador.capturar_pokemon(pokemon)

        print("Pokémon cadastrado.")

    elif opcao == "2":
        print("POKÉMONS DA POKÉDEX:")
        print("")

        pokemons = pokedex.listar_pokemons()

        if len(pokemons) == 0:
            print("Nenhum Pokémon cadastrado.")
        else:
            for pokemon in pokemons:
                print(pokemon.imprimir_dados())
    elif opcao == "3":
        print("POKÉMONS DE ÁGUA:")
        print("")
        for pokemon in pokedex.listar_pokemons():
            if pokemon.tipo == "Água":
                print(pokemon.imprimir_dados())
    elif opcao == "4":
        print("POKÉMONS DE FOGO:")
        print("")
        for pokemon in pokedex.listar_pokemons():
            if pokemon.tipo == "Fogo":
                print(pokemon.imprimir_dados())

    elif opcao == "5":
        print("POKÉMONS CAPTURADOS:")
        print("")

        pokemons = treinador.listar_pokemons()

        if len(pokemons) == 0:
            print("Nenhum Pokémon capturado.")
        else:
            for pokemon in pokemons:
                print(pokemon.imprimir_dados())

    elif opcao == "0":
        print("Saindo da Pokédex.")
        break

    else:
        print("Opção inválida!")

