import random
from gamev2 import palavras


lista = palavras


def game():
     
    print("\nBem-vindo(a) ao jogo da forca!")
    print("Adivinhe a palavra abaixo:\n")
    word = random.choice(lista)
    
    wrong_letters = []

    tries = 7

    discover_letters = ["_" for letter in word]

    while tries > 0:

        print(" ".join(discover_letters))
        print("\nRemanining tries: ", tries)
        print("Wrong Letter", " ".join(wrong_letters))

        attempt = input("\nType a letter: ").lower()

        if len(attempt) != 1 or not attempt.isalpha():
            print("Por favor, digite apenas uma letra válida.")
            continue

        if attempt in discover_letters or attempt in wrong_letters:
            print("Você já tentou essa letra!")
            continue
        
        if attempt in word:
            for index, letter in enumerate(word):
                if attempt == letter:
                    discover_letters[index] = letter
        else:
            wrong_letters.append(attempt)
            tries -= 1

        if "_" not in discover_letters:
            print("\nParabens você venceu!\n A palavra era", word.upper())    
            break
        
    if "_" in discover_letters:
        print("\nVocê perdeu tente novamente!\n A palavra era", word.upper())

game()



