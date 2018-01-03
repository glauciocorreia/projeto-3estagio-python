#=====================================================================================================================================================================================#

#MAIN/PRINCIPAL

'''
Sistemas para Internet
1º período
2017.2

Projeto Algoritmos e Programação
Professor: Lamark

Aluno: Gláucio Correia Dutra
E-mail: glauciocorreiaa@gmail.com
Matricula: 1720020743

Avaliação Terceiro Estágio
'''

#=====================================================================================================================================================================================#

'''
O "main.py" é onde o programa será rodado, usando as funções desenvolvidas em "fuctions.py". Por mais que esse arquivo seja o principal, a essência de todo o código importante está
em "functions.py", assim como anotações e explicações do que foi pedido e de como tudo foi feito.
'''

#=====================================================================================================================================================================================#


from functions import *							#Importando todas as funções/itens criadas em "functions.py"

txt = open('convidados.txt', 'r')				#Lendo o arquivo de texto 'convidados.txt' e salvando na variável "txt"
lista = func_convidados(txt)					#O retorno da função "func_convidados(txt)" é armazenado na variável "lista"
txt.close()										#Fechando o arquivo

doc = func_pdf(lista)							#O retorno da função "func_pdf(lista)" é armazenado na variável "doc"

func_email()									#Ativando a função "func_email()"

