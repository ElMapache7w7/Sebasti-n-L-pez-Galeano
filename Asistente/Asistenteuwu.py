import speech_recognition as sr
import pyttsx3
import webbrowser
import wikipedia
import datetime

# Inicializar el motor de texto a voz
engine = pyttsx3.init()

# Nombre del asistente
ASISTENTE_NOMBRE = "Asistente"

# Función para convertir texto a voz
def hablar(texto):
    engine.say(texto)
    engine.runAndWait()

# Función para reconocer comandos por voz
def escuchar_comando():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Escuchando...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        try:
            comando = r.recognize_google(audio, language='ES-MX')
            print(f"Has dicho: {comando}\n")
            return comando.lower()
        except sr.UnknownValueError:
            hablar("No entendí lo que dijiste, por favor intenta de nuevo.")
            return ""
        except sr.RequestError as e:
            hablar("Hubo un problema con el servicio de reconocimiento de voz.")
            return ""

# Función para obtener la hora actual
def obtener_hora():
    hora_actual = datetime.datetime.now().strftime("%H:%M:%S")
    hablar(f"La hora actual es {hora_actual}")
    print(f"La hora actual es {hora_actual}")

# Función para buscar en Wikipedia
def buscar_wikipedia(consulta):
    hablar(f"Buscando {consulta} en Wikipedia...")
    try:
        resultado = wikipedia.summary(consulta, sentences=2, auto_suggest=False)
        hablar("Esto es lo que encontré en Wikipedia:")
        hablar(resultado)
        print(resultado)
    except wikipedia.exceptions.DisambiguationError as e:
        hablar("Hay varias opciones para esa búsqueda. Intenta ser más específico.")
        print(e.options)
    except wikipedia.exceptions.PageError:
        hablar("No encontré ningún resultado para esa búsqueda.")
        print("No se encontró ningún resultado.")
    except Exception as e:
        hablar("Hubo un error al realizar la búsqueda en Wikipedia.")
        print(f"Error: {e}")

# Función para buscar en YouTube
def buscar_youtube(cancion):
    hablar(f"Buscando {cancion} en YouTube.")
    
    # Buscar en YouTube usando el navegador
    query = cancion.replace(' ', '+')
    url = f"https://www.youtube.com/results?search_query={query}"
    
    webbrowser.open(url)
    hablar(f"Aquí tienes los resultados para {cancion} en YouTube.")

# Función para abrir Google
def abrir_google():
    hablar("Abriendo Google.")
    webbrowser.open("https://www.google.com")

# Función principal para procesar comandos
def ejecutar_comando(comando):
    if ASISTENTE_NOMBRE.lower() in comando:
        if "hora" in comando:
            obtener_hora()
        elif "wikipedia" in comando:
            hablar("¿Qué quieres buscar en Wikipedia?")
            consulta = escuchar_comando()
            if consulta:
                buscar_wikipedia(consulta)
        elif "youtube" in comando:
            hablar("¿Qué canción o video quieres buscar en YouTube?")
            cancion = escuchar_comando()
            if cancion:
                buscar_youtube(cancion)
        elif "google" in comando:
            abrir_google()
        else:
            hablar("Lo siento, no entiendo ese comando.")

# Ciclo principal del asistente
if __name__ == "__main__":
    hablar(f"Hola, soy {ASISTENTE_NOMBRE}. ¿En qué te puedo ayudar?")
    while True:
        comando = escuchar_comando()
        ejecutar_comando(comando)
