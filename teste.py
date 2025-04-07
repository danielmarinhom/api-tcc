import json
import base64
with open("response.json", 'r') as f:
    base_audio = f.read()
    data = json.loads(base_audio)
    base_text = data['audio_base64']
with open("audio_reconstruido.mp3", "wb") as mp3_file:
    mp3_file.write(base64.b64decode(base_text))