import speech_recognition as sr
import time

def recognize_speech():
    recognizer = sr.Recognizer()
    time.sleep(1)
    with sr.Microphone() as source:
        time.sleep(1)
        recognizer.adjust_for_ambient_noise(source, duration = 0.2)
        print("****************************")
        print("  INICIANDO RECONOCIMIENTO")
        print("****************************")
        print("Di algo...")
        try:
            audio = recognizer.listen(source)
        except sr.WaitTimeoutError:
            print("Se agoto el tiempo")
        except sr.UnknownValueError:
            print("Ni idea loco")
        except sr.RequestError as e:
            print("Problemas amigo: {O}".format(e))
        time.sleep(1)
    try:
        text = recognizer.recognize_google(audio, language = "es-ES")
        print("Baxter entendio: " + text)
        return(text.encode('utf-8'))
    except sr.UnknownValueError:
        print("Baxter no pudo entender lo que dijiste")
        return("")
    except sr.RequestError as e:
        print("Could not request results from Speech Recognition service; {0}".format(e))
        return("")

#recognize_speech()