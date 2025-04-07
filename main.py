import audio_to_base64

from flask import Flask, jsonify, request

app = Flask(__name__, template_folder='./')

#APPLICATION ROUTES
#INDEX
@app.route('/', methods=['POST'])
def index():
    data = request.get_json()
    if not data or not "Text" in data:
        return jsonify({"error": "Campo 'Text' é obrigatório!"}), 400
    
    text = data['Text']
    audio_base64 = audio_to_base64.start(text)
    return jsonify({"audio_base64": audio_base64})

if __name__ == '__main__':
    app.run(debug=True)