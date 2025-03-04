from flask import Flask, request, jsonify

app = Flask(__name__)

# Definir la clave API que se debe usar
API_KEY = '2f5ae96c-b558-4c7b-a590-a501ae1c3f6c'

@app.route('/DevOps', methods=['POST'])
def devops():
    # Obtener la API Key de los encabezados de la solicitud
    api_key = request.headers.get('X-Parse-REST-API-Key')

    # Verificar si la API Key es correcta
    if api_key != API_KEY:
        return "ERROR: Unauthorized", 403  # Responder con 403 si la API Key no es válida

    # Obtener la carga útil (payload) del cuerpo de la solicitud
    data = request.get_json()

    # Verificar si los campos necesarios están presentes en la carga útil
    if 'message' not in data or 'to' not in data or 'from' not in data or 'timeToLifeSec' not in data:
        return "ERROR: Bad Request", 400  # Si faltan campos, responder con 400

    # Responder con el mensaje esperado
    to = data['to']
    response_message = f"Hello {to} your message will be send"

    return jsonify({"message": response_message})

# Manejar otros métodos HTTP que no sean POST
@app.route('/DevOps', methods=['GET', 'PUT', 'DELETE', 'PATCH'])
def handle_other_methods():
    return "ERROR", 405  # Responder con 405 Method Not Allowed para otros métodos HTTP

if __name__ == '__main__':
    app.run(debug=True)
