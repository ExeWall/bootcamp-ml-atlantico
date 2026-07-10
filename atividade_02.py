"""
Curso: Básico em Machine Learning - Atlântico Avanti
Atividade: 02 (Somativa)
Aluno: Wallyson Rodrigues da Silva
"""
import pandas as pd
import numpy as np

# ==============================================================================
# 1. Escreva uma função que receba uma lista de números e retorne outra lista 
#    com os números ímpares.
# ==============================================================================
def filtrar_impares(lista):
    impares = []
    for num in lista:
        if num % 2 != 0:  
            impares.append(num)
    return impares

# ==============================================================================
# 2. Escreva uma função que receba uma lista de números e retorne outra lista 
#    com os números primos presentes.
# ==============================================================================
def filtrar_primos(lista):
    primos = []
    for num in lista:
        if num > 1:
            e_primo = True
            for i in range(2, num):
                if num % i == 0:
                    e_primo = False
                    break
            if e_primo:
                primos.append(num)
    return primos

# ==============================================================================
# 3. Escreva uma função que receba duas listas e retorne outra lista com os 
#    elementos que estão presentes em apenas uma das listas.
# ==============================================================================
def elementos_unicos_entre_listas(lista1, lista2):
    resultado = []
    for item in lista1:
        if item not in lista2 and item not in resultado:
            resultado.append(item)
    for item in lista2:
        if item not in lista1 and item not in resultado:
            resultado.append(item)
    return resultado

# ==============================================================================
# 4. Dada uma lista de números inteiros, escreva uma função para encontrar o 
#    segundo maior valor na lista.
# ==============================================================================
def segundo_maior(lista):
    lista_unica = list(set(lista))
    if len(lista_unica) < 2:
        return None 
    
    lista_unica.sort()
    return lista_unica[-2] 

# ==============================================================================
# 5. Crie uma função que receba uma lista de tuplas, cada uma contendo o 
#    nome e a idade de uma pessoa, e retorne a lista ordenada pelo nome das 
#    pessoas em ordem alfabética.
# ==============================================================================
def ordenar_por_nome(lista_pessoas):
    return sorted(lista_pessoas, key=lambda x: x[0])

# ==============================================================================
# 6. Como identificar e tratar outliers em uma coluna numérica usando desvio 
#    padrão ou quartis?
# ==============================================================================
"""
Resposta:
Outliers são aqueles valores muito fora da curva (extremos). Podemos resolver assim:

* Usando Quartis (MÉTODO IQR): A gente calcula a diferença entre o terceiro e o 
  primeiro quartil (IQR = Q3 - Q1). Qualquer valor menor que (Q1 - 1.5 * IQR) ou 
  maior que (Q3 + 1.5 * IQR) é um outlier.
  
* Usando Desvio Padrão: A gente calcula a média e o desvio padrão da coluna. 
  Geralmente, dados que estão a mais de 3 desvios padrões de distância da média 
  são considerados outliers.

Tratamento: Para tratar, eu posso apagar essas linhas do DataFrame se forem poucas, 
ou "capar" os valores, substituindo os que passaram do limite pelo valor máximo permitido.
"""

# ==============================================================================
# 7. Como concatenar vários DataFrames (empilhando linhas ou colunas), 
#    mesmo que tenham colunas diferentes?
# ==============================================================================
"""
Resposta:
Para juntar vários DataFrames usamos a função `pd.concat()`. 
- Se a ideia for empilhar um embaixo do outro (adicionar linhas), usamos axis=0.
- Se a ideia for colar um ao lado do outro (adicionar colunas), usamos axis=1.

Se eles tiverem colunas ou linhas diferentes, o Pandas vai juntar tudo mesmo assim. 
Onde faltar informação (por exemplo, um DataFrame tinha a coluna 'A' mas o outro 
não tinha), ele preenche esses buracos automaticamente com NaN (valores nulos).
"""

# ==============================================================================
# 8. Utilizando pandas, como realizar a leitura de um arquivo CSV em um 
#    DataFrame e exibir as primeiras linhas?
# ==============================================================================
"""
Resposta:
Para ler o arquivo, usamos a função `pd.read_csv()`. Para mostrar os primeiros 
dados da tabela (por padrão as 5 primeiras linhas), usamos o método `.head()`.

Exemplo de código:
df = pd.read_csv('nome_do_arquivo.csv')
print(df.head())
"""

# ==============================================================================
# 9. Utilizando pandas, como selecionar uma coluna específica e filtrar linhas 
#    em um "DataFrame" com base em uma condição?
# ==============================================================================
"""
Resposta:
- Para pegar uma coluna específica, a gente passa o nome dela entre colchetes: df['nome_da_coluna'].
- Para filtrar as linhas com uma condição, colocamos a regra que queremos dentro de colchetes no DataFrame.

Exemplo de código:
# Filtrando apenas as pessoas que têm mais de 18 anos na coluna 'idade'
maiores_de_idade = df[df['idade'] > 18]
"""

# ==============================================================================
# 10. Utilizando pandas, como lidar com valores ausentes (NaN) em um DataFrame?
# ==============================================================================
"""
Resposta:
O Pandas dá duas formas principais e bem diretas para tratar os NaN:

1. Apagar os nulos: Se quisermos deletar as linhas que têm qualquer campo vazio, 
   usamos o método `.dropna()`.
   
2. Preencher os nulos: Se quisermos substituir o vazio por algum valor fixo, pela 
   média da coluna ou por um texto, usamos o método `.fillna()`.

Exemplo de código:
# Preenchendo os campos vazios da coluna 'nota' com zero
df['nota'] = df['nota'].fillna(0)
"""