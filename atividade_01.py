"""
Curso: Machine Learning
Atividade: 01
Aluno: Wallyson Rodrigues da Silva
"""

# ==============================================================================
# 1. Explique, com suas palavras, o que é machine learning?
# ==============================================================================
"""
Resposta:
Para mim, Machine Learning é uma forma de ensinar o computador a resolver um 
problema mostrando exemplos para ele, em vez de criar regras estritas no código. 
No desenvolvimento tradicional, a gente escreve regras como "se acontecer isso, 
faça aquilo". No Machine Learning é o contrário: a gente joga um monte de dados 
do que já aconteceu no passado e o algoritmo descobre sozinho o padrão daquilo.

Exemplo: Se eu quiser que o sistema identifique se um e-mail é spam, eu não fico 
bloqueando palavra por palavra manualmente. Eu entrego milhares de e-mails que 
já sei que são spam e o sistema aprende a reconhecer os padrões de texto e 
remetente que indicam uma mensagem maldosa.
"""

# ==============================================================================
# 2. Explique o conceito de conjunto de treinamento, conjunto de validação e 
#    conjunto de teste em machine learning.
# ==============================================================================
"""
Resposta:
Quando estamos criando um modelo, não podemos usar todos os dados de uma vez só, 
senão não temos como saber se ele realmente aprendeu ou só decorou. Por isso, 
dividimos os dados em três partes:

* Treinamento: É a maior parte dos dados. É por onde o modelo estuda e tenta 
  aprender os padrões do problema. É como se fossem os exercícios de fixação que 
  a gente faz em sala de aula.
  
* Validação: É um pedaço menor que usamos enquanto o modelo ainda está sendo 
  construído. Serve para dar uma checada se ele está indo pelo caminho certo ou 
  se está "viciado" nos dados de treino. Funciona como um simulado antes da prova.
  
* Teste: É a última parte, separada lá no começo e que o modelo nunca viu. 
  A gente só usa quando o modelo está pronto para ver como ele se sai com dados 
  totalmente novos. É a prova final para testar o desempenho real do sistema.
"""

# ==============================================================================
# 3. Explique como você lidaria com dados ausentes em um conjunto de dados 
#    de treinamento.
# ==============================================================================
"""
Resposta:
Se eu encontrasse campos vazios ou informações faltando no meu conjunto de dados, 
eu avaliaria três caminhos principais dependendo da situação:

1. Apagar os dados: Se forem pouquíssimas linhas com erro e eu tiver muitos dados 
   sobrando, eu simplesmente deletaria essas linhas para não atrapalhar o modelo.
   
2. Preencher com a média/mediana: Se for uma coluna de números (como a idade de 
   clientes), eu poderia calcular a média ou a mediana de todo mundo e colocar 
   esse valor nos campos que estão vazios. É uma solução simples e que não joga 
   dados fora.
   
3. Preencher com a moda: Se for uma informação de categoria (como o estado onde 
   a pessoa mora), eu preencheria com o valor que mais se repete nos dados.
"""

# ==============================================================================
# 4. O que é uma matriz de confusão e como ela é usada para avaliar o 
#    desempenho de um modelo preditivo? 
# ==============================================================================
"""
Resposta:
A matriz de confusão é uma tabela simples que mostra onde o nosso modelo acertou 
e onde ele errou (ou se "confundiu"). Ela cruza o resultado real com o que o 
modelo previu.

Pensando em um teste de gravidez, por exemplo, a matriz mostra quatro cenários:
- O teste diz que deu positivo e a pessoa realmente está grávida (Acerto).
- O teste diz que deu negativo e a pessoa realmente não está grávida (Acerto).
- O teste diz que deu positivo, mas a pessoa NÃO está grávida (Erro - Falso Positivo).
- O teste diz que deu negativo, mas a pessoa ESTÁ grávida (Erro - Falso Negativo).

Olhando para essa tabela, a gente consegue calcular o desempenho do modelo além 
da acurácia geral, descobrindo se ele é melhor pegando os casos positivos ou 
evitando alarmes falsos.
"""

# ==============================================================================
# 5. Em quais áreas (tais como construção civil, agricultura, saúde, manufatura, 
#    entre outras) você acha mais interessante aplicar algoritmos de machine 
#    learning?
# ==============================================================================
"""
Resposta:
As duas áreas que eu acho mais interessantes e que vejo muito potencial são:

1. Saúde: Acho incrível usar modelos para analisar exames de imagem, como raios-X 
   ou tomografias. O algoritmo pode ajudar a apontar pequenas alterações bem no 
   início de uma doença, servindo como um braço direito para o médico dar um 
   diagnóstico mais rápido.

2. Agricultura: Acho muito massa aplicar ML no campo usando sensores no solo ou 
   imagens de drone. Dá para prever a quantidade de colheita, descobrir pragas 
   antes que elas destruam a plantação inteira e até economizar água, colocando 
   irrigação só onde o solo realmente precisa.
"""