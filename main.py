#!/usr/bin/env python
# coding=utf-8

import speech
import nlp
import conversation

import sys
import time
import rospy
import baxter_interface

from threading import Thread

# Inicializa el "nodo" ROS y lo registra "with the Master"
rospy.init_node('Main_Control')

keywords = {
	"izquierdo", "izquierda", "derecho", "derecha",
	"brazo", "brazos", "mano", "manos",
	"levanta", "estira", "sacude", "abre"
}
'''
actions = {
	########## ACCIONES SIMPLES #############
	"levanta el brazo izquierdo": ("simple", "./src/baxter_camilo_movements/raise_elbow_left.py"),
	"levanta el brazo derecho": ("simple", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	"estira el brazo izquierdo": ("simple", "./src/baxter_camilo_movements/open_left.py"),
	"estira el brazo derecho": ("simple", "./src/baxter_camilo_movements/open_right.py"),
	"levanta la mano izquierda": ("simple", "./src/baxter_camilo_movements/raise_hand_left.py"),
	"levanta la mano derecha": ("simple", "./src/baxter_camilo_movements/raise_hand_right.py"),
	"sacude la mano izquierda": ("simple", "./src/baxter_camilo_movements/shake_hand_left.py"),
	"sacude la mano derecha": ("simple", "./src/baxter_camilo_movements/shake_hand_right.py"),
	"endereza el codo izquierdo": ("simple", "./src/baxter_camilo_movements/elbow_straight_left.py"),
	"endereza el codo derecho": ("simple", "./src/baxter_camilo_movements/elbow_straight_right.py"),
	"adelanta el hombro izquierdo": ("simple", "./src/baxter_camilo_movements/forward_elbow_left.py"),
	"adelanta el hombro derecho": ("simple", "./src/baxter_camilo_movements/forward_elbow_right.py"),
	"quiebra la muneca izquierda": ("simple", "./src/baxter_camilo_movements/break_wrist_left.py"),
	"quiebra la muneca derecha": ("simple", "./src/baxter_camilo_movements/break_wrist_right.py"),
	"sonrie": ("simple", "./src/baxter_camilo_movements/smile.py"),
	"dunno_face": ("simple", "./src/baxter_camilo_movements/dunno_face.py"),
	"pon cara enojada": ("simple", "./src/baxter_camilo_movements/angry.py"),
	"izquierda arriba abajo": ("simple", "./src/baxter_camilo_movements/celebration_left.py"),
	"derecha arriba abajo": ("simple", "./src/baxter_camilo_movements/celebration_right.py"),
	"conversemos": ("simple", "./src/baxter_camilo_movements/conversation.py"),
	########## ACCIONES PARALELAS ###########
	"preparate": ("paralela", "./src/baxter_camilo_movements/home_pos.py", "./src/baxter_camilo_movements/home_right.py"),
	"abre los brazos": ("paralela", "./src/baxter_camilo_movements/open_right.py", "./src/baxter_camilo_movements/open_left.py"),
	"levanta los brazos": ("paralela", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	"sacude las manos": ("paralela", "./src/baxter_camilo_movements/shake_hand_left.py", "./src/baxter_camilo_movements/shake_hand_right.py"),
	"adelanta los hombros": ("paralela", "./src/baxter_camilo_movements/forward_elbow_left.py", "./src/baxter_camilo_movements/forward_elbow_right.py"),
	"quiebra las munecas": ("paralela", "./src/baxter_camilo_movements/break_wrist_left.py", "./src/baxter_camilo_movements/break_wrist_right.py"),
	########## ACCIONES COMPUESTAS ##########
	"di que si": ("compuesta", "./src/baxter_camilo_movements/smile.py", "./src/baxter_camilo_movements/answer_yes.py", "./src/baxter_camilo_movements/std_face.py"),
	"di que no": ("compuesta", "./src/baxter_camilo_movements/angry.py", "./src/baxter_camilo_movements/answer_no.py", "./src/baxter_camilo_movements/std_face.py"),
	"saluda": ("compuesta", "./src/baxter_camilo_movements/raise_elbow_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/shake_hand_right.py"),
	"saluda izquierda": ("compuesta", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/shake_hand_left.py"),
	"celebra izquierda": ("compuesta", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/elbow_straight_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/celebration_left.py"),
	"celebra derecha": ("compuesta", "./src/baxter_camilo_movements/raise_elbow_right.py", "./src/baxter_camilo_movements/elbow_straight_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/celebration_right.py"),
	"dunno_left": ("compuesta", "./src/baxter_camilo_movements/elbow_straight_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/dunno_left.py"),
	"dunno_right": ("compuesta", "./src/baxter_camilo_movements/elbow_straight_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/dunno_right.py"),
	########## ACCIONES COMPLEJAS ###########
	"saluda con ambas manos": ("compleja", "paralela", ("instruccion", "instruccion"), "saluda", "saluda izquierda"),
	"da un abrazo": ("compleja", "secuencial", ("instruccion", "instruccion", "instruccion", "instruccion"), "levanta los brazos", "adelanta los hombros", "adelanta los hombros", "quiebra las munecas"),
	"celebra": ("compleja", "paralela", ("instruccion", "instruccion"), "celebra izquierda", "celebra derecha"),
	"dunno": ("compleja", "paralela", ("instruccion", "instruccion"), "dunno_left", "dunno_right")
}
'''
actions = {
	########## ACCIONES SIMPLES #############
	("terminar",): ("", "", ""),
	("conversar",): ("", "", ""),
	("levanta", "brazo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/raise_elbow_left.py"),
	("sube", "brazo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/raise_elbow_left.py"),
	("levanta", "brazo", "derecho"): ("simple", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	("sube", "brazo", "derecho"): ("simple", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	("estira", "brazo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/open_left.py"),
	("estira", "brazo", "derecho"): ("simple", "./src/baxter_camilo_movements/open_right.py"),
	("levanta", "mano", "izquierda"): ("simple", "./src/baxter_camilo_movements/raise_hand_left.py"),
	("sube", "mano", "izquierda"): ("simple", "./src/baxter_camilo_movements/raise_hand_left.py"),
	("levanta", "mano", "derecha"): ("simple", "./src/baxter_camilo_movements/raise_hand_right.py"),
	("sube", "mano", "derecha"): ("simple", "./src/baxter_camilo_movements/raise_hand_right.py"),
	("sacude", "mano", "izquierda"): ("simple", "./src/baxter_camilo_movements/shake_hand_left.py"),
	("sacude", "mano", "derecha"): ("simple", "./src/baxter_camilo_movements/shake_hand_right.py"),
	("endereza", "codo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/elbow_straight_left.py"),
	("endereza", "codo", "derecho"): ("simple", "./src/baxter_camilo_movements/elbow_straight_right.py"),
	("adelanta", "hombro", "derecho"): ("simple", "./src/baxter_camilo_movements/forward_elbow_right.py"),
	("adelanta", "hombro", "izquierdo"): ("simple", "./src/baxter_camilo_movements/forward_elbow_left.py"),
	("quiebra", "muñeca", "derecha"): ("simple", "./src/baxter_camilo_movements/break_wrist_right.py"),
	("quiebra", "muñeca", "izquierda"): ("simple", "./src/baxter_camilo_movements/break_wrist_left.py"),
	("sonrie",): ("simple", "./src/baxter_camilo_movements/smile.py"),
	("cara", "pregunta"): ("simple", "./src/baxter_camilo_movements/dunno_face.py"),
	("poner", "enojar"): ("simple", "./src/baxter_camilo_movements/angry.py"),
	("izquierda", "arriba", "abajo"): ("simple", "./src/baxter_camilo_movements/celebration_left.py"),
	("derecha", "arriba", "abajo"): ("simple", "./src/baxter_camilo_movements/celebration_right.py"),
	########## ACCIONES PARALELAS ###########
	("preparate",): ("paralela", "./src/baxter_camilo_movements/home_pos.py", "./src/baxter_camilo_movements/home_right.py"),
	("abre", "brazos"): ("paralela", "./src/baxter_camilo_movements/open_right.py", "./src/baxter_camilo_movements/open_left.py"),
	("estira", "brazos"): ("paralela", "./src/baxter_camilo_movements/open_right.py", "./src/baxter_camilo_movements/open_left.py"),
	("levanta", "brazos"): ("paralela", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	("sube", "brazos"): ("paralela", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	("sacude", "manos"): ("paralela", "./src/baxter_camilo_movements/shake_hand_left.py", "./src/baxter_camilo_movements/shake_hand_right.py"),
	("adelanta", "hombros"): ("paralela", "./src/baxter_camilo_movements/forward_elbow_left.py", "./src/baxter_camilo_movements/forward_elbow_right.py"),
	("quiebra", "muñecas"): ("paralela", "./src/baxter_camilo_movements/break_wrist_left.py", "./src/baxter_camilo_movements/break_wrist_right.py"),
	########## ACCIONES COMPUESTAS ##########
	("decir", "si"): ("compuesta", "./src/baxter_camilo_movements/smile.py", "./src/baxter_camilo_movements/answer_yes.py", "./src/baxter_camilo_movements/std_face.py"),
	("asentir",): ("compuesta", "./src/baxter_camilo_movements/smile.py", "./src/baxter_camilo_movements/answer_yes.py", "./src/baxter_camilo_movements/std_face.py"),
	("decir", "no"): ("compuesta", "./src/baxter_camilo_movements/angry.py", "./src/baxter_camilo_movements/answer_no.py", "./src/baxter_camilo_movements/std_face.py"),
	("negar",): ("compuesta", "./src/baxter_camilo_movements/angry.py", "./src/baxter_camilo_movements/answer_no.py", "./src/baxter_camilo_movements/std_face.py"),
	("saludar", "derecho"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/shake_hand_right.py"),
	("saludar", "izquierdo"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/shake_hand_left.py"),
	("celebrar", "izquierdo"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/elbow_straight_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/celebration_left.py"),
	("celebrar", "derecho"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_right.py", "./src/baxter_camilo_movements/elbow_straight_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/celebration_right.py"),
	("incognita", "izquierdo"): ("compuesta", "./src/baxter_camilo_movements/elbow_straight_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/dunno_left.py"),
	("incognita", "derecho"): ("compuesta", "./src/baxter_camilo_movements/elbow_straight_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/dunno_right.py"),
	########## ACCIONES COMPLEJAS ###########
	("saluda", "manos"): ("compleja", "paralela", ("instruccion", "instruccion"), ("saludar", "derecho"), ("saludar", "izquierdo")),
	("abrazo",): ("compleja", "secuencial", ("instruccion", "instruccion", "instruccion", "instruccion"), ("levanta", "brazos"), ("adelanta", "hombros"), ("adelanta", "hombros"), ("quiebra", "muñecas")),
	("abrazala",): ("compleja", "secuencial", ("instruccion", "instruccion", "instruccion", "instruccion"), ("levanta", "brazos"), ("adelanta", "hombros"), ("adelanta", "hombros"), ("quiebra", "muñecas")),
	("abrazalo",): ("compleja", "secuencial", ("instruccion", "instruccion", "instruccion", "instruccion"), ("levanta", "brazos"), ("adelanta", "hombros"), ("adelanta", "hombros"), ("quiebra", "muñecas")),
	("abrazame",): ("compleja", "secuencial", ("instruccion", "instruccion", "instruccion", "instruccion"), ("levanta", "brazos"), ("adelanta", "hombros"), ("adelanta", "hombros"), ("quiebra", "muñecas")),
	("celebrar",): ("compleja", "paralela", ("instruccion", "instruccion"), ("celebrar", "izquierdo"), ("celebrar", "derecho")),
	("celebrar", "ambos"): ("compleja", "paralela", ("instruccion", "instruccion"), ("celebrar", "izquierdo"), ("celebrar", "derecho")),
	("decir", "no", "saber"): ("compleja", "paralela", ("instruccion", "instruccion"), ("incognita", "izquierdo"), ("incognita", "derecho")),
}

def searching_actions(tup):
	for i in actions.keys():
		cont = 0
		aux = ()
		for j in tup:
			for k in i:
				if j == k:
					cont = cont + 1
					aux = aux + (j,)
		if cont == len(i):
			return i
	return ("",)

def input_selection():
	ch = ""
	while(ch != "1" and ch != "2"):
		print("Seleccione el formato de entrada:")
		print("(1) Texto escrito")
		print("(2) Voz hablada")
		ch = raw_input("")
	return ch


def thread_function(path):
	with open(path) as f:
		exec(f.read())

def complex_function(args):
	for i in range(1, len(args)):
		thread_function(args[i])

def standard_pose():
	with open("./src/baxter_camilo_movements/std_face.py") as f:
		exec(f.read())
	path = actions[("preparate",)]
	ll = []
	cont = 0
	for i in range(1, len(path)):
		cont += 1
		ll.append(Thread(target = thread_function, args = (path[i],)))
		ll[cont-1].start()
	for i in ll:
		i.join()

def dunno_pose():
	with open("./src/baxter_camilo_movements/dunno_face.py") as f:
		exec(f.read())
	path = actions[("decir", "no", "saber")]
	aux = 2
	cont = 0
	ll = []
	for i in path[2]:
		aux += 1
		if path[aux] in actions:
			path2 = actions[path[aux]]
			ll.append(Thread(target = complex_function, args = (path2,)))
			ll[cont-1].start()
	for i in ll:
		i.join()
	time.sleep(2)

def main():
	textInput = ""
	choise = input_selection()
	while textInput != ("terminar",):
		if(choise == "2"):
			textInput = speech.recognize_speech()
		else:
			textInput = raw_input("Ingrese accion: ")
		textInput = nlp.clean_vowels(textInput)

		aux = searching_actions(nlp.tokenization(textInput))
		if aux == ("",):
			aux = searching_actions(nlp.lemmatization(textInput))
		textInput = aux


		if textInput in actions:
			path = actions[textInput]
			print("Ejecutando accion...")
			
			if textInput == ("conversar",):
				print("*************************")
				print("Iniciando conversacion...")
				print("*************************")
				print("")
				while 1:
					if(choise == "2"):
						pregunta = speech.recognize_speech()
					else:
						pregunta = raw_input("Ingrese pregunta: ")
						pregunta = pregunta + '?'
					if pregunta == "silencio":
						print("Entendido, terminando conversacion...")
						print("")
						print("")
						break
					respuesta = conversation.obtener_respuesta(pregunta)
					if respuesta[0] == 'S':
						print("Si")
						path = actions[("decir", "si")]
						for i in range(1, len(path)):
							thread_function(path[i])
					elif respuesta == 'No':
						print("No")
						path = actions[("decir", "no")]
						for i in range(1, len(path)):
							thread_function(path[i])
					else:
						print("No se")
						standard_pose()
						dunno_pose()
						standard_pose()
			elif path[0] == "simple":
				# EJECUCION ACCION SIMPLE
				thread_function(path[1])
			elif path[0] == "paralela":
				# EJECUCION ACCION PARALELA
				ll = []
				for i in range(1, len(path)):
					ll.append(Thread(target = thread_function, args = (path[i],)))
					ll[i-1].start()
				for i in ll:
					i.join()
			elif path[0] == "compuesta":
				#EJECUCCION ACCION COMPUESTA
				for i in range(1, len(path)):
					thread_function(path[i])
			else:
				# EJECUCION ACCION COMPLEJA
				aux = 2
				if path[1] == "secuencial":
					for i in path[2]:
						aux += 1
						if i == "instruccion":
							if path[aux] in actions:
								path2 = actions[path[aux]]
								if path2[0] == "simple":
									thread_function(path2[1])
								elif path2[0] == "paralela":
									ll = []
									for j in range(1, len(path2)):
										ll.append(Thread(target = thread_function, args = (path2[j],)))
										ll[j-1].start()
									for j in range(len(ll)):
										ll[j].join()
								elif path2[0] == "compuesta":
									for j in range(1, len(path2)):
										thread_function(path2[j])
						elif i == "codigo":
							thread_function(path[aux])
				elif path[1] == "paralela":
					for i in path[2]:
						aux += 1
						if i == "instruccion":
							if path[aux] in actions:
								path2 = actions[path[aux]]
								if path2[0] == "simple":
									Thread(target = thread_function, args =(path2[1],)).start()
								elif path2[0] == "paralela":
									ll = []
									for j in range(1, len(path2)):
										##Thread(target = thread_function, args = (path2[j],)).start()  # Posiblemente asi para paralela
										ll.append(Thread(target = thread_function, args = (path2[j],)))
										ll[j-1].start()
									for j in range(len(ll)):
										ll[j].join()
								elif path2[0] == "compuesta":
									t1 = Thread(target = complex_function, args = (path2,))
									t1.start()
									t1.join()
						elif i == "codigo":
							t1 = Thread(target = thread_function, args = (path[aux],))
							t1.start()
							t1.join()
		elif textInput == ("terminar",):
			print("Finalizando programa...")
		else:
			print("Accion no encontrada")

			###### COLOCAR IMAGEN EN PANTALLA ######
			standard_pose()

			dunno_pose()

			standard_pose()

			###### COLOCAR IMAGEN EN PANTALLA ######

			print("Reintente...")



if __name__ == '__main__':
	sys.exit(main())