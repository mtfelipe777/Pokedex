from pokemon_agua import PokemonAgua
from pokemon_fogo import PokemonFogo
from pokemon import Pokemon
from pokedex import Pokedex
from treinador import Treinador


pokedex = Pokedex()

nome_treinador = input("Digite o nome do treinador: ")
treinador = Treinador(nome_treinador)

while True:
    print()
    print("POKÉDEX:")
    print()
    print("1 - Cadastrar Pokémon")
    print("2 - Listar todos os Pokémons")
    print("3 - Listar Pokémons de água")
    print("4 - Listar Pokémons de fogo")
    print("5 - Ver Pokémon capturados")
    print("6 - Adicionar Pokémon a equipe")
    print("7 - Deletar Pokémon da equipe")
    print("8 - Listar equipe")
    print("0 - Sair")
    print()

    opcao = input("Digite uma opção: ")
    print()

    if opcao == "1":
        print("CADASTRAR POKÉMON")
        print()
        nome = input("Nome do Pokémon: ")
        tipo = input("Tipo do Pokémon: ")
        nivel = int(input("Nível do Pokémon: "))
        capturado = input("O Pokémon foi capturado? (sim/não): ")
        if tipo == "agua":
            pokemon = PokemonAgua(nome, tipo, nivel, capturado)
        elif tipo == "fogo":
            pokemon = PokemonFogo(nome, tipo, nivel, capturado)
        else:
            pokemon = Pokemon(nome, tipo, nivel, capturado)

        pokedex.adicionar_pokemon(pokemon)

        if capturado == "sim":
            treinador.capturar_pokemon(pokemon)

        print("Pokémon cadastrado.")
        print()

    elif opcao == "2":
        print("POKÉMONS DA POKÉDEX:")
        print()

        pokemons = pokedex.listar_pokemons()

        if len(pokemons) == 0:
            print("Nenhum Pokémon cadastrado.")
            print()
        else:
            for pokemon in pokemons:
                print(pokemon.imprimir_dados())
                print()

    elif opcao == "3":
        print("POKÉMONS DE ÁGUA:")
        print()
        for pokemon in pokedex.listar_pokemons():
            if pokemon.tipo == "agua":
                print(pokemon.imprimir_dados())

    elif opcao == "4":
        print("POKÉMONS DE FOGO:")
        print()
        for pokemon in pokedex.listar_pokemons():
            if pokemon.tipo == "fogo":
                print(pokemon.imprimir_dados())

    elif opcao == "5":
        print("POKÉMONS CAPTURADOS:")
        print()

        pokemons = treinador.listar_pokemons()

        if len(pokemons) == 0:
            print("Nenhum Pokémon capturado.")
            print()
        else:
            for pokemon in pokemons:
                print(pokemon.imprimir_dados())
                print()

    elif opcao == "6":
        print("ADICIONAR A EQUIPE")
        print()

        nome = input("Digite o nome do Pokémon: ")
        print()
        for pokemon in pokedex.listar_pokemons():
            if pokemon.nome == nome:

                if pokemon.capturado == "sim":
                    if treinador.equipe.adicionar_pokemon(pokemon):
                        print("Pokémon adicionado à equipe!")
                        print()
                    else:
                        print("A equipe já possui 3 Pokémon.")
                        print()
                else:
                    print("Esse Pokémon não foi capturado.")
                    print()

                break
    elif opcao == "7":
        print("REMOVER DA EQUIPE:")
        print()
        nome = input("Informe o nome do pokémon que você quer deletar: ")
        if treinador.equipe.remover_pokemon(nome):
            print("Pokémon removido da equipe!")
            print()
        else:
            print("Pokémon não encontrado na equipe.")
            print()
    elif opcao == "8":
        print(treinador.equipe.listar_pokemons())
        print()

    elif opcao == "0":
        print("Saindo da Pokédex.")
        break

    else:
        print("Opção inválida!")

