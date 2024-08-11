import sqlite3
#_________________________________________________________________
# def crear_db():
#     '''Función para crear una nueva base de datos si es que aún no existe'''
#     conn = sqlite3.connect('logs.db')
#     cursor = conn.cursor()
#     cursor.execute('''
#         CREATE TABLE IF NOT EXISTS service_logs (
#             id INTEGER PRIMARY KEY AUTOINCREMENT,
#             timestamp TEXT,
#             received_at TEXT,
#             service_name TEXT,
#             severity TEXT,
#             message TEXT
#         )
#     ''')
#     conn.commit()
#     conn.close()
#________________________________________________________________
def cargar_datos(timestamp, received_at, service_name, severity, message):
    '''Función para agregar datos recibidos de los logs'''
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('''
        INSERT INTO service_logs (
            timestamp, 
            received_at, 
            service_name, 
            severity, 
            message
        ) VALUES (?, ?, ?, ?, ?)
    ''', (timestamp, received_at, service_name, severity, message))
    conn.commit()
    conn.close()
#________________________________________________________________
def registros_entre_fechas(fecha_inicio,fecha_final):
    '''Función para obtener registros entre un rango de fechas'''
    # fecha_inicio = '2024-08-01 00:00:00' ejemplos
    # fecha_fin = '2024-08-08 23:59:59'
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute('''SELECT * FROM service_logs 
                   WHERE received_at BETWEEN ? AND ?
                   ORDER BY received_at ASC''',
                   (fecha_inicio,fecha_final))
    registros = cursor.fetchall()
    conn.close()
    return registros
#__________________________________________________________________
def extraer_datos():
    conn = sqlite3.connect('logs.db')
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM service_logs")
    datos = cursor.fetchall()
    conn.close()
    return datos

# d=registros_entre_fechas('2024-08-09 11:51:21', '2024-08-11 10:55:38')
# print(d)
# crear_db()





