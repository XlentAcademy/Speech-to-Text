from flask import Flask, render_template, request, redirect, Response
from gtts import gTTS

app = Flask(__name__)

# Class for converting text to Speech using google text to speech api
class tts:
    '''
    Text to speech converts your text to audio file with the help google text to speech api.
    Default language, lang='en'
    You have to pass some text.
    '''
    def __init__(self, text, lang='en'):
        self.text = text
        self.language = lang
        self.path = './static/sample.wav'
    def run(self):
        obj = gTTS(text=self.text, lang=self.language, slow=False)
        obj.save(str(self.path))

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        try:
            text = request.form['textbox']
            convert = tts(text=text)
            convert.run()
        except AssertionError:
            return render_template('warn.html')
        return render_template('index.html', text=text)
    else:
        return render_template('index.html')

@app.route("/wav")
def streamwav():
    def generate():
        with open("./static/sample.wav", "rb") as fwav:
            data = fwav.read(1024)
            while data:
                yield data
                data = fwav.read(1024)
    return Response(generate(), mimetype="audio/x-wav")

@app.route("/delete")
def delete():
    try:
        import os
        os.remove("./static/sample.wav")
    except FileNotFoundError:
        return redirect('/')
    return redirect('/')

@app.route("/about")
def about():
    return render_template('about.html')

@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html')

if __name__ == "__main__":
    app.run(debug=True, port=7000)