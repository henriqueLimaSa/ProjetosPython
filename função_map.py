#A função map é utilizada para aplicar uma determinada função em cada elemento de
# um iterável (lista, tupla, dicionários etc.), retornando um novo iterável com os valores modificados.
lista = [1,2,3,4,5,6,7,8,9,10]

def multiplicar_por(iten):
    return iten*2

def main():
    nova_lista = list(map(multiplicar_por,lista))
    print(nova_lista)

if __name__ == "__main__":
    main()


#utilizando a função map e lambda
lista = [1,2,3,4,5,6,7,8,9,10]

def main():
    nova_lista = list(map(lambda numero: numero*2,lista))
    print(nova_lista)


if __name__ == "__main__":
    main()