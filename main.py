from flask import Flask, request
import subprocess

app = Flask(__name__)

@app.route('/github-webhook', methods=['POST'])
def github_webhook():
    payload = request.json
    print("Webhook recibido:", payload)

    # Aquí puedes ejecutar tu código o script
    # Por ejemplo, ejecutar un script Python:
    subprocess.run(["python3", "mi_script.py"])

    return "OK", 200

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
