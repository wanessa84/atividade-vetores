
import numpy as np
# ------------------------------------
# 1. Criar uma lista e acessar um elemento
# ------------------------------------
lista = [10, 20, 30, 40, 50]
print(lista[2])  # Exibe o terceiro elemento (índice 2)

# ------------------------------------
# 2. Modificar um elemento da lista
# ------------------------------------
lista[1] = 99  # Substitui o segundo elemento (índice 1) por 99
print(lista)

# ------------------------------------
# 3. Adicionar e remover elementos da lista
# ------------------------------------
lista.append(60)  # Adiciona 60 ao final
lista.pop(0)  # Remove o primeiro elemento
print(lista)

# ------------------------------------
# 4. Ordenar a lista
# ------------------------------------
lista.sort()  # Ordem crescente
print("Ordenado crescente:", lista)
lista.sort(reverse=True)  # Ordem decrescente
print("Ordenado decrescente:", lista)

# ------------------------------------
# 5. Soma e média dos valores da lista
# ------------------------------------
soma = sum(lista)
media = soma / len(lista)
print(f"Soma: {soma}, Média: {media}")

# ------------------------------------
# 6. Criar e acessar uma tupla
# ------------------------------------
tupla = ("Alice", "Bruno", "Carlos", "Daniela")
print(tupla[1])  # Segundo nome (índice 1)

# ------------------------------------
# 7. Converter tupla para lista e modificar
# ------------------------------------
lista_temp = list(tupla)
lista_temp[2] = "Clara"
tupla = tuple(lista_temp)
print(tupla)

# ------------------------------------
# 8. Verificar se um valor está na tupla
# ------------------------------------
print("Carlos" in tupla)  # Retorna True ou False

# ------------------------------------
# 9. Concatenar duas tuplas
# ------------------------------------
tupla1 = (1, 2, 3)
tupla2 = (4, 5, 6)
tupla3 = tupla1 + tupla2  # Une ambas as tuplas
print(tupla3)

# ------------------------------------
# 10. Encontrar o índice de um valor na tupla
# ------------------------------------
print(tupla3.index(4))  # Retorna a posição do número 4

# ------------------------------------
# 11. Criar um array NumPy e somar valores
# ------------------------------------
array = np.array([10, 20, 30, 40, 50])
print(array + 2)  # Adiciona 2 a cada elemento

# ------------------------------------
# 12. Multiplicar todos os elementos do array
# ------------------------------------
print(array * 3)  # Multiplica por 3

# ------------------------------------
# 13. Somar dois arrays
# ------------------------------------
array2 = np.array([1, 2, 3, 4, 5])
print(array + array2)  # Soma os arrays

# ------------------------------------
# 14. Média e desvio padrão de um array
# ------------------------------------
print("Média:", np.mean(array))
print("Desvio padrão:", np.std(array))

# ------------------------------------
# 15. Filtrar números pares do array
# ------------------------------------
print(array[array % 2 == 0])  # Apenas pares

# ------------------------------------
# 16. Criar um dicionário e acessar um valor
# ------------------------------------
produtos = {
    "Notebook": 3500,
    "Teclado": 150,
    "Mouse": 80
}
print(produtos["Teclado"])  # Exibe o preço do teclado

# ------------------------------------
# 17. Adicionar um produto e modificar um preço
# ------------------------------------
produtos["Monitor"] = 1200  # Adiciona um novo item
produtos["Notebook"] = 4000  # Altera o preço do notebook
print(produtos)

# ------------------------------------
# 18. Remover um item do dicionário
# ------------------------------------
del produtos["Mouse"]  # Remove o item "Mouse"
print(produtos)

# ------------------------------------
# 19. Percorrer o dicionário e exibir chave/valor
# ------------------------------------
for chave, valor in produtos.items():
    print(f"Produto: {chave}, Preço: R${valor}")

# ------------------------------------
# 20. Converter um dicionário em uma lista de tuplas
# ------------------------------------
lista_de_tuplas = list(produtos.items())
print(lista_de_tuplas)  # Exibe a conversão






