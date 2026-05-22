from gtts import gTTS
import os

texto = "Hola, este audio fue generado utilizando Python."

tts = gTTS(text=texto, lang='es', slow=False)

tts.save("audio_generado.mp3")

print("Audio generado correctamente.")

os.system("start audio_generado.mp3")