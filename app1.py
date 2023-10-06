import openai

def crear_imagen(descripcion):
    openai.api_key = "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"
    openai.Model.list()
    respuesta = openai.Image.create(
        prompt = descripcion,
        n=2,
        siz2="512x512"
    )
    return respuesta["data"][0]["url"]
if __name__ == "__main__":
    descripcion = input("Ingresa la descripcion de la imagen a generar: ")
    res = crear_imagen(descripcion)
    for url in res:
        print(url["url"])