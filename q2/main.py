from time import sleep

if __name__ == '__main__':
    alfabeto = [
        'A', 'B', 'C', 'D', 'E', 'F', 'G',
        'H', 'I', 'J', 'K', 'L', 'M', 'N',
        'O', 'P', 'Q', 'R', 'S', 'T', 'U',
        'V', 'W', 'X', 'Y', 'Z'
    ]
    palavra = input('Entre com uma palavra: ').strip().upper()
    palavra_codificada = []
    for letra in palavra:
        pos = alfabeto.index(letra)
        if pos != len(alfabeto) - 1:
            palavra_codificada.append(alfabeto[pos + 1])
        else:
            palavra_codificada.append(alfabeto[0])
    print(f'Codificando a palavra: {palavra}...')
    sleep(2)
    resultado = ''.join(palavra_codificada)
    print(f'Resultado: {resultado}')
