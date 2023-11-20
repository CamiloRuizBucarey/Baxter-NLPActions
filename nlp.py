# coding=utf-8

import spacy

def clean_vowels(s):
	replacements = (
		("á", "a"),
		("é", "e"),
		("í", "i"),
		("ó", "o"),
		("ú", "u"),
		)
	for a, b in replacements:
		s = s.replace(a, b)
	return s


actions = {
	########## ACCIONES SIMPLES #############
	("terminar",): ("",),
	("levanta", "brazo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/raise_elbow_left.py"),
	("levanta", "brazo", "derecho"): ("simple", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	("estira", "brazo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/open_left.py"),
	("estira", "brazo", "derecho"): ("simple", "./src/baxter_camilo_movements/open_right.py"),
	("levanta", "mano", "izquierda"): ("simple", "./src/baxter_camilo_movements/raise_hand_left.py"),
	("levanta", "mano", "derecha"): ("simple", "./src/baxter_camilo_movements/raise_hand_right.py"),
	("sacude", "mano", "izquierda"): ("simple", "./src/baxter_camilo_movements/shake_hand_left.py"),
	("sacude", "mano", "derecha"): ("simple", "./src/baxter_camilo_movements/shake_hand_right.py"),
	("endereza", "codo", "izquierdo"): ("simple", "./src/baxter_camilo_movements/elbow_straight_left.py"),
	("endereza", "codo", "derecho"): ("simple", "./src/baxter_camilo_movements/elbow_straight_right.py"),
	("adelanta", "hombro", "izquierdo"): ("simple", "./src/baxter_camilo_movements/forward_elbow_left.py"),
	("adelanta", "hombro", "derecho"): ("simple", "./src/baxter_camilo_movements/forward_elbow_right.py"),
	("quiebra", "muñeca", "izquierda"): ("simple", "./src/baxter_camilo_movements/break_wrist_left.py"),
	("quiebra", "muñeca", "derecha"): ("simple", "./src/baxter_camilo_movements/break_wrist_right.py"),
	("sonrie",): ("simple", "./src/baxter_camilo_movements/smile.py"),
	("cara", "pregunta"): ("simple", "./src/baxter_camilo_movements/dunno_face.py"),
	("poner", "enojar"): ("simple", "./src/baxter_camilo_movements/angry.py"),
	("izquierda", "arriba", "abajo"): ("simple", "./src/baxter_camilo_movements/celebration_left.py"),
	("derecha", "arriba", "abajo"): ("simple", "./src/baxter_camilo_movements/celebration_right.py"),
	("conversar",): ("simple", "./src/baxter_camilo_movements/conversation.py"),
	########## ACCIONES PARALELAS ###########
	("preparate",): ("paralela", "./src/baxter_camilo_movements/home_pos.py", "./src/baxter_camilo_movements/home_right.py"),
	("abre", "brazos"): ("paralela", "./src/baxter_camilo_movements/open_right.py", "./src/baxter_camilo_movements/open_left.py"),
	("levanta", "brazos"): ("paralela", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_elbow_right.py"),
	("sacude", "manos"): ("paralela", "./src/baxter_camilo_movements/shake_hand_left.py", "./src/baxter_camilo_movements/shake_hand_right.py"),
	("adelanta", "hombros"): ("paralela", "./src/baxter_camilo_movements/forward_elbow_left.py", "./src/baxter_camilo_movements/forward_elbow_right.py"),
	("quiebra", "muñecas"): ("paralela", "./src/baxter_camilo_movements/break_wrist_left.py", "./src/baxter_camilo_movements/break_wrist_right.py"),
	########## ACCIONES COMPUESTAS ##########
	("decir", "si"): ("compuesta", "./src/baxter_camilo_movements/smile.py", "./src/baxter_camilo_movements/answer_yes.py", "./src/baxter_camilo_movements/std_face.py"),
	("decir", "no"): ("compuesta", "./src/baxter_camilo_movements/angry.py", "./src/baxter_camilo_movements/answer_no.py", "./src/baxter_camilo_movements/std_face.py"),
	("saludar", "derecho"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/shake_hand_right.py"),
	("saludar", "izquierdo"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/shake_hand_left.py"),
	("celebrar", "izquierdo"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_left.py", "./src/baxter_camilo_movements/elbow_straight_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/celebration_left.py"),
	("celebrar", "derecho"): ("compuesta", "./src/baxter_camilo_movements/raise_elbow_right.py", "./src/baxter_camilo_movements/elbow_straight_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/celebration_right.py"),
	("incognita", "izquierdo"): ("compuesta", "./src/baxter_camilo_movements/elbow_straight_left.py", "./src/baxter_camilo_movements/raise_hand_left.py", "./src/baxter_camilo_movements/dunno_left.py"),
	("incognita", "derecho"): ("compuesta", "./src/baxter_camilo_movements/elbow_straight_right.py", "./src/baxter_camilo_movements/raise_hand_right.py", "./src/baxter_camilo_movements/dunno_right.py"),
	########## ACCIONES COMPLEJAS ###########
	("saluda", "manos"): ("compleja", "paralela", ("instruccion", "instruccion"), ("saludar", "derecho"), ("saludar", "izquierdo")),
	("abrazo",): ("compleja", "secuencial", ("instruccion", "instruccion", "instruccion", "instruccion"), ("levanta", "brazos"), ("adelanta", "hombros"), ("adelanta", "hombros"), ("quiebra", "muñecas")),
	("celebrar",): ("compleja", "paralela", ("instruccion", "instruccion"), ("celebrar", "izquierdo"), ("celebrar", "derecho")),
	("decir", "no", "saber"): ("compleja", "paralela", ("instruccion", "instruccion"), ("incognita", "izquierdo"), ("incognita", "derecho"))
}
'''
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
'''

#	RECIBE UN TEXTO, APLICA NORMALIZACION, Y DEVUELVE UNA TUPLA CON LAS PALABRAS
def tokenization(text):
	nlp = spacy.load('es_core_news_sm')
	text = unicode(text, "utf-8")
	doc = nlp(text)
	tokens = [t.orth_ for t in doc if not t.is_punct | t.is_stop]
	tokens = [t.lower() for t in tokens if t.isalpha()]
	words = ()
	for i in tokens:
		words = words + (str(i),)
	return words

#	RECIBE UN TEXTO, APLICA LEMATIZACION, Y DEVUELVE UNA TUPLA CON LAS PALABRAS
def lemmatization(text):
	nlp = spacy.load('es_core_news_sm')
	text = unicode(text, "utf-8")
	doc = nlp(text)
	lemmas = [tok.lemma_.lower() for tok in doc if not tok.is_punct]
	words = ()
	for i in lemmas:
		i = clean_vowels(str(i))
		words = words + (str(i),)
	return words
'''
texto = "baxter mi loco, celebra usando tus dos manos"
print("Palabras resultantes de tokenizacion:")
aux = tokenization(texto)
print(aux, type(aux))
aux = searching_actions(aux)
if aux == ("",):
	print("DALEEEEEEEEEEEEE")
print("**************")
print("Palabras resultantes de lematizacion:")
aux = lemmatization(texto)
print(aux, type(aux))
print(searching_actions(aux))
'''