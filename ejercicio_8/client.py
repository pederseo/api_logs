from flask import Flask, request, render_template, redirect, url_for
from datetime import datetime
import requests
import random

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        service = request.form['service']
        level = request.form['error']

        api_keys = ["1234", "5678", "9101", "1213"]

        url = 'http://localhost:5000/log'

        timestamp = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        service_name = service
        severity = level
        message = ''
        if severity == 'DEBUG':
            message = "El valor de la variable X es 42."
        elif severity == 'INFO':
            message = "El servicio se inició correctamente."
        elif severity == 'WARNING':
            message = "El archivo de configuración no se encontró, usando valores por defecto."
        elif severity == 'ERROR':
            message = "Error al conectar con la base de datos."
        elif severity == 'CRITICAL':
            message = "Fallo en el sistema: memoria insuficiente."
        elif severity == 'FATAL':
            message = "Fallo irrecuperable, cerrando la aplicación."
            
#________________________________estructura del JSON___________________________________________
        headers = {
            'Content-Type': 'application/json',
            'Authorization': random.choice(api_keys)
        }
        log_data = {
            'timestamp': timestamp,
            'service_name': service_name,
            'severity': severity,
            'message': message
        }

        response = requests.post(url, json=log_data, headers=headers)
        print(response.json())  # Imprimir la respuesta del servidor

    return render_template('index.html')

if __name__ == '__main__':
    app.run(port=5001)

