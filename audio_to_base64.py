import os
import pyttsx3
import base64

#text = "Sim, os rádios e as TVs vieram antes da internet. O rádio surgiu no final do século XIX e se popularizou no início do século XX, com as primeiras transmissões públicas por volta de 1920. Já a televisão começou a ser desenvolvida nas décadas de 1920 e 1930, e as primeiras transmissões regulares começaram nos anos 1940. A internet, por sua vez, começou a ser desenvolvida na década de 1960, mas se popularizou apenas nas décadas de 1990 e 2000, com o advento da World Wide Web (WWW) e a expansão do acesso público à rede. Portanto, os rádios e as TVs são tecnologias bem anteriores à internet."

def start(text: str):
    engine = pyttsx3.init()  # Usa eSpeak no Linux automaticamente
    engine.setProperty('rate', 200)   
    engine.save_to_file(text, "audio_file.mp3")
    engine.runAndWait()
    return convert(text)

def convert(text: str):
    # converte pra base64
    file_name = "audio_file.mp3"
    with open(file_name, "rb") as audio_file:
        audio_bytes = audio_file.read()
        audio_base64 = base64.b64encode(audio_bytes).decode("utf-8")
    os.remove(file_name)
    return audio_base64