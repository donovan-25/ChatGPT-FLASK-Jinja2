from flask import Flask, request, render_template
import openai

app = Flask(__name__)

imagenes = []

@app.route('/', methods=["GET", "POST"])
def peticion():
    if request.method == 'POST':
        descripcion = request.form.get("descripcion")
        num_img = int(request.form.get("num_img"))
        for _ in range(num_img):
            url_img = crear_imagen(descripcion)
            imagenes.append(url_img)
    return render_template('index.html', imagenes=imagenes)

def crear_imagen(descripcion):
    openai.api_key = "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"
    respuesta = openai.Image.create(
            prompt=descripcion,
            n=1,
            size="512x512"
        )
    return respuesta["data"][0]["url"]

if __name__ == "_main_":
    app.run(debug=True, port=5000)