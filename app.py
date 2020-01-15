from models import Pokemon, Types


def main():
    pikachu = Pokemon("Pikachu", Types.ELECTRIC, 25)
    eevee = Pokemon("Eevee", Types.NORMAL, 133)
    print(pokemon_to_str(pikachu))


def prepend_indefinite_article(str: str) -> str:
    vowels = "aeiou"
    return f"an {str}" if str[0].lower() in vowels else "a {str}"


def pokemon_to_str(pokemon: Pokemon) -> str:
    return (
        f"{pokemon.name} is #{pokemon.number}. "
        f"It is {prepend_indefinite_article(pokemon.type.name)} type Pokemon."
    )


if __name__ == '__main__':
    main()
