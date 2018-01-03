#=====================================================================================================================================================================================#

#FUNÇÕES

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
O projeto do terceiro estágio tem como objetivo pôr em prática o conteúdo aprendido durante todo o desenvolvimento da disciplina Algoritmos e Programação. A linguagem utilizada 
para criar os itens solicitados deverá ser Python, a partir da versão 3.

Este trabalho será composto por 5 partes, que devem ser feitas de forma sequencial e complementar.
'''

#=====================================================================================================================================================================================#

#Seção de importação de libs/módulos em "fuctions.py", sendo "smtplib" já nativa no Python e "reportlab" instalada pelo "Pip"

#Importando lib/módulo "Reportlab" (item "canvas", especificamente), focada na criação e manipulação de arquivos PDF dentro do Python

from reportlab.pdfgen import canvas									

#Importando lib/módulo "smtplib" e alguns itens focadas para ajustes e envio de e-mails dentro do Python

import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

#=====================================================================================================================================================================================#

'''
1) [5 Pontos] Fazer uma análise no arquivo convidados.txt, verificando seu conteúdo, como as informações estão separadas e organizadas. Em seguida, é necessário coletar todos os 
dados e organizar em um dicionário contendo apenas as seguintes informações nome como chave e telefone como valor. Deverá ser feita uma função que receba umaString (Str) com os 
dados do arquivo e retorne o dicionário. 
'''

#=====================================================================================================================================================================================#

#Definindo a função que irá ler o arquivo "convidados.txt" (string) e irá retornar um dicionário, onde o nome de cada indivíduo será a 'chave' e o telefone o 'valor'.

def func_convidados(txt):											#Definição da função

	convidados = {}													#Criação do dicionário em branco

	txt_linhas = txt.readlines()									#Leitura do arquivo .txt (string), o transformando em uma lista

	for linx in txt_linhas[1:]:										#Laço para ler linha por linha, desconsiderando a primeira linha da lista e considerando todo o resto
		lista = linx.split()										#Criação da variável "lista" onde irá remover o espaço (" ") na linha lida, registrando esses novos dados
		for liny in lista:											#Laço para verificar a linha na nova variável "lista"
			nome,telefone = liny.split('-')							#Remoção do hífen/traço ("-") no indíce da lista que está sendo lido
			convidados[nome] = telefone								#Organização das chaves e dos valores no dicionário "convidados"
	return convidados												#Retorna o dicionário "convidados", com os nomes do convidados como chave e os telefones dos convidados como valor

#=====================================================================================================================================================================================#

'''
2) [2 Pontos] O dicionário resultante do item anterior deverá ser usado para gerar um pdf [com o formato de uma lista de nomes com seus respectivos telefones]
'''

#=====================================================================================================================================================================================#

#Definindo a função que irá pegar o parametro "lista" e transformar e organizar em um arquivo PDF

def func_pdf(lista):												#Definição da função

	doc = canvas.Canvas("Contatos.pdf")								#Criando um arquivo PDF com nome "Contatos.pdf", o atribuindo à "doc"
	doc.setLineWidth(.2)											#Estipulando a espessura das linhas no arquivo

	doc.setFont('Helvetica-Bold', 14)								#Definindo o tipo e tamanho da fonte a partir desse momento (Tipo: Helvetica-Bold; Tamanho: 14)
	doc.drawString(170,700,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')	#Desenhando/escrevendo um simples componente para o visual da página
	doc.setFont('Helvetica-Bold', 16)								#Definindo o tipo e tamanho da fonte a partir desse momento (Tipo: Helvetica-Bold; Tamanho: 16)
	doc.drawString(220,660,'----Lista de Contatos----')				#Desenhando/escrevendo um texto-título para a lista de contatos na página
	doc.setFont('Helvetica-Bold', 12)								#Definindo o tipo e tamanho da fonte a partir desse momento (Tipo: Helvetica; Tamanho: 12)
	doc.drawString(250,595,'Nome e Telefone')						#Desenhando/escrevendo um texto-subtítulo para a lista de contatos na página	
		
	y = 580															#Definindo que a variável "y" (eixo) terá o valor "580" ("posição/pontuação" indo ao canto inferior da página) 
	doc.setFont('Helvetica', 12)									#Definindo o tipo e tamanho da fonte a partir desse momento (Tipo: Helvetica-Bold; Tamanho: 14)
	for nome,telefone in lista.items():								#Laço de repetição que irá passar por cada item de "lista"
		y -= 15 													#A primeita etapa do laço é diminuir em 15 pontos/posição o eixo Y ("de cima para baixo")
		doc.drawString(250,y, '{} : {}'.format(nome,telefone))		#Irá desenhar/escrever na página a chave e o valor lidos (Nome e Telefone) na posição x = 250 e y estipulada acima

	doc.setFont('Helvetica-Bold', 14)								#Definindo o tipo e tamanho da fonte a partir desse momento (Tipo: Helvetica-Bold; Tamanho: 14)
	doc.drawString(170,y-40,'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx')	#Desenhando/escrevendo um simples componente para o visual da página

	doc.save()														#Salvando todas as modificações do arquivo PDF em "doc"

	return doc														#Retorna "doc" com o arquivo pdf (Contatos.pdf) com todas as alterações feitas

#=====================================================================================================================================================================================#

'''
3) [1 Ponto] O arquivo pdf gerado deverá ser enviado por e-mail para o seguinte:

Endereço: app.p1.unipe@gmail.com
Assunto: Contatos – Equipe [nome_da_equipe]
Conteúdo: Segue os contatos em anexo.
Anexar documento
'''

#=====================================================================================================================================================================================#

def func_email():																		#Definição da função

	fromaddr = "glaucio.spi.unipe@gmail.com"											#Estipulando o remetente do e-mail
	toaddr = "app.p1.unipe@gmail.com"													#Estipulando o destinatário do e-mail

	msg = MIMEMultipart()																#Construindo o "header" do e-mail

	msg['From'] = fromaddr																#Selecionando o remetente
	msg['To'] = toaddr																	#Selecionando o destinatário
	msg['Subject'] = "Contatos - Equipe Gláucio Correia Dutra"							#Estipulando o "Assunto" do e-mail

	body = "Seguem os contatos em anexo!"												#Conteúdo do "Corpo" do e-mail												

	msg.attach(MIMEText(body, 'plain'))													#Inserindo o "body" como texto

	filename = "Contatos.pdf"															#Estipulando o nome do arquivo binário em PDF a ser anexado
	attachment = open(filename, "rb")													#Abrindo (lendo documento binário ("rb")) o arquivo em PDF e vinculando à variável "attachment"

	part = MIMEBase('application', 'octet-stream')										#Processo necessário para codificar o arquivo PDF para anexo - parte 1
	part.set_payload((attachment).read())												#Processo necessário para codificar o arquivo PDF para anexo - parte 2
	encoders.encode_base64(part)														#Processo necessário para codificar o arquivo PDF para anexo - parte 3
	part.add_header('Content-Disposition', "attachment; filename= %s" % filename)		#Processo necessário para codificar o arquivo PDF para anexo - parte 4

	msg.attach(part)																	#Inserindo o anexo ao e-mail		

	server = smtplib.SMTP('smtp.gmail.com', 587)										#Configurando SMTP e porta do GMAIL
	server.starttls()																	#Configurando componentes de segurança
	server.login(fromaddr, "testes789")													#Realizando login, selecionando o e-mail e inserindo a senha de acesso
	text = msg.as_string()																#Transformando o conteúdo do e-mail em string
	server.sendmail(fromaddr, toaddr, text)												#Enviando e-mail selecionando o e-mail do remetente, do destinatário e o conteúdo do e-mail
	server.quit()																		#Saindo do servidor do e-mail

#=====================================================================================================================================================================================#