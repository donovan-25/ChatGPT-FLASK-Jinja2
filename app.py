from flask import Flask, request,render_template
import openai

app = Flask(__name__)

historial = []

@app.route('/', methods = ["GET","POST"])
def index():
    if request.method =='POST':
        pregunta=request.form.get("pregunta")
        resultado=enviar_pregunta(pregunta)
        historial.append(("Yo", pregunta))
        historial.append(("ChatGPT", resultado))
    else:
        resultado=""

    return render_template ('index.html', historial=historial)

def enviar_pregunta(pregunta):
    openai.api_key = "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"
    respuesta = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[
            {"role": "system", "content": "You are a helpful assistant."},
            {"role": "user", "content": pregunta}
        ],
    )
    respuesta_texto = respuesta["choices"][0]["message"]["content"]
    return respuesta_texto

if __name__ == "_main_":
    app.run(debug=True, port=5000)