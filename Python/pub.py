# -*- coding: utf-8 -*-
import paho.mqtt.client #Importa o módulo client do paho 
import paho.mqtt.publish #Importa o módulo publish do paho

#Função de callback para conexão 
def on_connect(client, userdata, flags, rc):
	if rc == 0: #Se o código de retorno (rc) for 0, houve conexão
		print("Connectado")
	else: 
		print(f"Code: {rc}") #Senão, exibe o código de retorno a fim de verificar o erro 
#broker = "127.0.0.1"
broker = input('Insira o endereço IP do broker: ') #Recebe o endereço IPv4 do broker 
port = 1883 #porta na qual o broker escuta
t = input("Insira o tópico no qual deseja publicar: ") #t recebe uma string referente ao nome do tópico
while True:
	q = int(input("Define o nível de QoS da publicação [0-2]: ")) #q recebe o parâmetro de qos
	if 0<=q<=2:  #O qual deve estrar entre 0 e 2
		break #Dessa forma, quebre o laço, senão continue até o parâmetro estar correto 
while True: #Repita o processo de recebimento da mensagem e de envio  
	try:
		msg = input("você> ") #Recebimento da mensagem
		#Método responsável por publicar a mensagem
		paho.mqtt.publish.single( 
			topic=t, #Tópico 
			payload=msg, #Mensagem a ser enviada
			qos=q, #Nível de qos
			hostname=broker, #Endereço do broker
			port =port #Porta na qual opera
		)
	except:
		print('Erro inesperado ... Abortando processo')#Trativa de erro


