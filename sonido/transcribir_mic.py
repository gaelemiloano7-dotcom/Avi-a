import speech_recognition as sr
import keyboard

def listar_dispositivos():
    print("Dispositivos de audio disponibles:")
    for index, name in enumerate(sr.Microphone.list_microphone_names()):
        print(f"{index}: {name}")

def SpeechToText(device_index=None):
    Ai = sr.Recognizer()
    with sr.Microphone(device_index=device_index) as source:
        print("Hablando presiona 'q' para detener la grabación...")
        listening = Ai.listen(source, phrase_time_limit=6)
    try:
        command = Ai.recognize_google(listening, language="es-ES")
        print(f"Has dicho:" + command)
        with open("transcripcion_mic.txt", "a", encoding="utf-8") as file:
            file.write(command + "\n")
    
    except sr.UnknownValueError:
        print("No se pudo entender el audio")

print("dispositivos de audio disponibles:")
listar_dispositivos()

indice = int(input("Selecciona el índice del dispositivo de audio que deseas usar: "))
print("Presiona 'q' para comenzar a grabar...")
while True:
    if keyboard.is_pressed('q'):
        print("Se presionó 'q', saliendo del programa...")
        break
    else:
        SpeechToText(device_index=indice)