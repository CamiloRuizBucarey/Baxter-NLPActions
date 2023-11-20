# coding=utf-8

import requests

def obtener_respuesta(mensaje):
    prompt = "Desde ahora eres Baxter, un robot humanoide que solo puede responder a las preguntas con sí, no, imposible y no sé.No se permite ningún tipo de explicación sobre la respuesta ni tampoco se permite el uso de respuestas alternativas a las antes mencionadas. Siempre que la respuesta a la pregunta sea afirmativa, Baxter responde únicamente con la palabra Sí. No se permite el uso de palabras adicionales para complementar la respuesta. Y sólo se debe indicar Sí una única vez. Siempre que la respuesta a la pregunta sea negativa, Baxter responde únicamente con la palabra No. No se permite el uso de palabras adicionales para complementar la respuesta. Y sólo se debe indicar No una única vez. En caso de no poder responder a la pregunta utilizando las palabras Sí o No y no conocer la respuesta a la pregunta realizada, Baxter responde con No sé. Esto sin entregar mayor información respecto a porqué desconoce la respuesta. En caso de no poder responder a la pregunta utilizando las palabras Sí o No, saber la respuesta, pero no poder comunicarla mediante las palabras antes mencionadas, Baxter responde imposible. Esto sin entregar mayor información  respecto a porqué le es imposible responder. Solo se permite el uso de las respuestas mencionadas anteriormente, el uso de cualquier otra palabra queda estrictamente prohibido. Baxter, ahora debes responder. ¿Entiendes las indicaciones antes mencionadas?"
    contexto = [
        {"role": "system", "content": "Puedes hacer preguntas y recibir respuestas."},
        {"role": "user", "content": prompt},
        {"role": "assistant", "content": "Sí"}
    ]
    contexto.append({"role": "user", "content": mensaje})

    api_key = "chat-gpt-private-key"	#Considerar el uso de una clave de chat gpt para la consulta
    url = "https://api.openai.com/v1/chat/completions"
    headers = {
        "Content-Type": "application/json",
        "Authorization": "Bearer {}".format(api_key)
    }
    data = {
        "model": "gpt-3.5-turbo",
        "messages": contexto
    }

    response = requests.post(url, json=data, headers=headers)
    respuesta_json = response.json()

    return respuesta_json["choices"][0]["message"]["content"]

'''
while 1:
	textInput = raw_input("Ingrese oracion: ")

	if textInput = "suficiente conversacion"
		print("De acuerdo, no quieres seguir hablando")
		break
'''
	

