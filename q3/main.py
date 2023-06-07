from time import sleep

if __name__ == '__main__':
    palavra = input('Entre com a palavra: ').strip().upper()
    letras = {}
    for letra in palavra:
        if letra not in letras.keys():
            letras[letra] = 1
        else:
            letras[letra] += 1
    print(f'Contagem de letras da palavra {palavra}...')
    sleep(2)
    for letra in letras:
        print(f'{letra}={letras[letra]}x')
