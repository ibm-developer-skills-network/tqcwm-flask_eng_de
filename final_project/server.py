from machinetranslation import translator
from flask import Flask, render_template, request
import json

app = Flask("Web Translator")

@app.route("/englishToGerman")
def englishToGerman():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to German"

@app.route("/germanToEnglish")
def germanToEnglish():
    textToTranslate = request.args.get('textToTranslate')
    # Write your code here
    return "Translated text to English"

@app.route("/")
def renderIndexPage():
    # Write the code to render template

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
