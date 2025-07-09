from flask import Flask, request, jsonify
import uuid
from datetime import datetime, timezone

app = Flask(__name__)

@app.route('/')
def home():
      return jsonify({
                "status": "online",
                "service": "Webhook Manus GPT - Render Deploy",
                "version": "1.0.0",
                "endpoint": "/receber-instrucao-gpt"
      })

@app.route('/receber-instrucao-gpt', methods=['POST'])
def receber():
      try:
                dados = request.get_json() or {}
                return jsonify({
                    "status": "recebida",
                    "delivery_id": str(uuid.uuid4()),
                    "message": "Instrução recebida com sucesso",
                    "timestamp": datetime.now(timezone.utc).isoformat(),
                    "dados_recebidos": dados
                })
except Exception as e:
        return jsonify({
                      "status": "erro",
                      "message": str(e)
        }), 400

@app.route('/health')
def health():
      return jsonify({"status": "healthy"})

if __name__ == '__main__':
      app.run(host='0.0.0.0', port=5000)
