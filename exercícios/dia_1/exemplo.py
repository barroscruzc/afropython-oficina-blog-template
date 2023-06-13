def show_oficina(lista):
    i = 0
    for item in lista:
        i += 1
       # print(str(i) + ' - ' + item)


my_list = ['codespace', 'python', 'git', 'Django']

show_oficina(my_list)


# 1
def verifica_vogal(caractere):
    vogais = ['a', 'e', 'i', 'o', 'u']
    for vogal in vogais:
        if caractere.lowcase() == vogal:
            return True
            break
        else:
            return False
            break


# 2
def verifica_par_impar(numero):
    if numero%2 == 0:
        return 'par'
    else:
        return 'impar'
    

# 3
def concatena_listas(lista_um, lista_dois):
    lista = []
    lista.extend(lista_um)
    lista.extend(lista_dois)
    return lista


# 4
def inverte_palavra(palavra):
    palavra_invertida = palavra[::-1]
    return palavra_invertida


# 5
def verifica_palindromo(palavra):
    palindromo = palavra.lowercase()
    return palindromo == palavra[::-1].lowercase()

print(verifica_palindromo('cacau'))
print(verifica_palindromo('arara'))