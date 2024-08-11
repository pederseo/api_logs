from flask import Flask, request, jsonify, render_template
from datetime import datetime
from db_logs import*

app = Flask(__name__)

# Lista de API keys válidas
AUTORIZATION_API_KEY = ["1234", "5678", "9101", "1213"]

@app.route('/')
def index():
    '''se muestran todos los logs registrados de los servicios'''
    datos = extraer_datos()
    logs = []
    for registro in datos:
        logs.append({
            'id': registro[0],
            'timestamp': registro[1],
            'received_at': registro[2],
            'service_name': registro[3],
            'severity': registro[4],
            'message': registro[5]
        })
    return jsonify(logs)


@app.route('/log', methods=['GET', 'POST'])
def log():
    '''se guardan los logs autentificados de los servicios'''
    service_api_key = request.headers.get('Authorization')  # Obtiene la API key del encabezado
    
    if service_api_key in AUTORIZATION_API_KEY:  # Verifica si la API key es válida
        data = request.json
        timestamp = data.get('timestamp')
        received_at = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        service_name = data.get('service_name')
        severity = data.get('severity')
        message = data['message']

        cargar_datos(timestamp, received_at, service_name, severity, message)
        return jsonify({"status": "success"}), 201
    
    else:
        return jsonify({"error": "Unauthorized"}), 401

@app.route('/filtrar_logs', methods=['GET', 'POST'])
def filtrar_logs():
    '''funcion para filtrar los logs por fecha de registro'''
    registros = extraer_datos()

    lista_logs = [registro[2] for registro in registros]

    if request.method == 'POST':
        fecha_inicio = request.form['inicio']
        fecha_final = request.form['final']

        resultado = registros_entre_fechas(fecha_inicio,fecha_final)

        return render_template('filtro.html',lista_logs=lista_logs, resultado=resultado)



    return render_template('filtro.html', lista_logs=lista_logs)

if __name__ == '__main__':
    app.run(port=5000)  # Ejecutar la aplicación en el puerto 5000
