#É utilizada para filtrar elementos de um iterável (lista, tupla, dicionários etc.).
# O filtro é realizado utilizando uma função, que deve ser capaz de retornar true ou false
# (verdadeiro ou falso) para cada elemento do iterável.

lista = [1,2,3,4,5,6,7,8,9,10]

def valor_impar(numero):
    return numero%2 != 0


def main():
    nova_lista = list(filter(valor_impar,lista))
    print("A nova lista com somente numeros impa são {}".format(nova_lista))

if __name__ == "__main__":
    main()
