from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/ejecutar', methods=['GET'])
def ejecutar_codigo():
    # Puedes pasar parámetros opcionales desde la URL, ejemplo: ?nombre=juan
    nombre = request.args.get('nombre', 'desconocido')
    print(f"Petición recibida de: {nombre}")

    # Ejecuta tu script
    subprocess.run(["python3", "mi.py"])

    return f"Código ejecutado por {nombre}", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
