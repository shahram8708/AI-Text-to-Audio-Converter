from flask import Flask, render_template, request, send_file
from gtts import gTTS
import os

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/convert', methods=['POST'])
def convert_text_to_audio():
    text = request.json['text']
    voice = request.json['voice']

    if text.strip() != "":
        tts = gTTS(text, lang=voice)
        tts.save("static/audio.mp3")  
        return send_file("static/audio.mp3", as_attachment=True)
    else:
        return "Please enter some text to convert."

if __name__ == '__main__':
    app.run(debug=True)
