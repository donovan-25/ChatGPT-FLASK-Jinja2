from flask import Flask, request, render_template
import openai

app = Flask(__name__)

historial = []

@app.route('/', methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        pregunta = request.form.get("pregunta")
        resultado = enviar_pregunta(pregunta)
        historial.append(("Usuario", pregunta))
        historial.append(("ChatGPT", resultado))
    return render_template('index.html', historial=historial)

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

if __name__ == "__main__":
    app.run(debug=True, port=5000)