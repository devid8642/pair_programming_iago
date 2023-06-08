from unicodedata import normalize

if __name__ == '__main__':
    inp = input('Entre com uma palavra ou frase: ')
    inp2 = inp.strip().upper().replace(' ', '')
    inp_normalizado = normalize('NFKD', inp2).encode('ASCII', 'ignore').decode('ASCII')
    aux = []
    pontuacoes = [
        '!', '?', '.', ',', ':',
        ';', '/', '(', ')', '-', '"',
        "'"
    ]
    for pont in pontuacoes:
        if pont in inp_normalizado:
            inp_normalizado = inp_normalizado.replace(pont, '')
    for i in range(len(inp_normalizado) - 1, -1, -1):
        if inp_normalizado[i] not in pontuacoes:
            aux.append(inp_normalizado[i])
    if inp_normalizado == ''.join(aux):
        print(f'{inp} é um palíndromo')
    else:
        print(f'{inp} não é um palíndromo')
