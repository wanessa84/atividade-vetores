import numpy as np

# 1. Criação e acesso
numeros = [10, 20, 30, 40, 50, 60, 70, 80]
print("O quinto elemento é:", numeros[4])

# 2. Removendo números ímpares
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = [num for num in numeros if num % 2 == 0]
print("Lista sem ímpares:", pares)

# 3. Verificação de item na lista
frutas = ["Banana", "Maçã", "Laranja", "Uva", "Pera"]
print("Maçã está na lista!" if "Maçã" in frutas else "Maçã não está na lista.")

# 4. Multiplicação de elementos
dobro = [num * 2 for num in numeros]
print("Lista multiplicada por 2:", dobro)

# 5. Invertendo a lista sem usar reverse()
invertida = numeros[::-1]
print("Lista invertida:", invertida)


# 6. Criando e acessando tupla
cidades = ("São Paulo", "Rio de Janeiro", "Belo Horizonte", "Curitiba", "Salvador", "Manaus")
print("Última cidade:", cidades[-1])


# 7. Convertendo tupla para lista e modificando
tupla = ("Maçã", "Banana", "Laranja", "Uva")
lista = list(tupla)
lista.remove("Laranja")
tupla_modificada = tuple(lista)
print("Nova tupla:", tupla_modificada)


# 8. Concatenando tuplas
todas_cores = ("Azul", "Verde", "Vermelho") + ("Preto", "Branco", "Amarelo")
print("Tupla concatenada:", todas_cores)


# 9. Verificando presença de elemento
print("Python está na tupla!" if "Python" in ("Python", "Java", "C", "JavaScript", "Ruby") else "Python não está na tupla.")


# 10. Encontrando índice de um elemento
numeros_tupla = (10, 20, 30, 40, 50, 60)
print("Índice do número 50:", numeros_tupla.index(50))


# 11. Criando array NumPy com números aleatórios
array = np.random.randint(1, 101, size=10)
print("Array aleatório:", array)


# 12. Multiplicando por -1
negativo = array * -1
print("Array negativo:", negativo)


# 13. Substituindo valores maiores que 50
array[array > 50] = 50
print("Array modificado:", array)


# 14. Diferença entre elementos de dois arrays
diferenca = np.array([5, 10, 15, 20]) - np.array([1, 5, 10, 15])
print("Diferença entre arrays:", diferenca)


# 15. Encontrando o menor e o maior valor
print("Menor valor:", np.min(array))
print("Maior valor:", np.max(array))


# 16. Criando e acessando dicionário
paises = {"Brasil": "Brasília", "Argentina": "Buenos Aires", "França": "Paris"}
print("A capital do Brasil é:", paises["Brasil"])


# 17. Modificando dicionário
paises["Argentina"] = "Mendoza"
print("Novo dicionário:", paises)


# 18. Adicionando novo país
paises["Espanha"] = "Madri"
print("Dicionário atualizado:", paises)

# 19. Removendo um país
del paises["França"]
print("Dicionário após remoção:", paises)

# 20. Convertendo dicionário para listas
print("Lista de chaves:", list(paises.keys()))
print("Lista de valores:", list(paises.values()))



