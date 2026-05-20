import speech_recognition as sr

filename = "audio.wav"
output_file = "transcription_audio.txt"

r = sr.Recognizer()

try:
    with sr.AudioFile(filename) as source:
        duration = int(source.DURATION)
        full_transcription = ""
        print("Procesando el audio...")
        for i in range(0, duration, 10):
            try:  # Process audio in 5-second chunks
                audio = r.record(source,  duration=10)
                text = r.recognize_google(audio, language="es-ES")
                full_transcription += text + "\n"
                print(f"fragmento {i // 10 + 1}: {text}")
            except sr.UnknownValueError:
                print(f"fragmento {i // 10 + 1}: {text}: no se pudo entender el audio")
                full_transcription += "[no se pudo entender el audio]\n"
            except sr.RequestError as e:
                print(f"fragmento {i // 10 + 1}: {text}: error al comunicarse con el servicio de google; {e}")
                break
        
        with open(output_file, "w", encoding="utf-8") as f:
            f.write(full_transcription)

        print(f"Transcripción completa guardada en {output_file}")

except FileNotFoundError:
    print(f"Archivo {filename} no encontrado. Asegúrate de que el archivo de audio esté en el mismo directorio que este script o proporciona la ruta correcta.")
except ValueError as e:
    print(f"Error al procesar el archivo de audio: {e}")
except Exception as e:
    print(f"Ocurrió un error inesperado: {e}")