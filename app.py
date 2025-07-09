  pforrotm  =f lianstk( oism.peonrvti rFolna.sgke,t (r'ePqOuReTs't,,  1j0s0o0n0i)f)y

   f r o ma pfpl.arsukn_(choorsst =i'm0p.o0r.t0 .C0O'R,S 
   piomrpto=rpto rutu)id, os
   from datetime import datetime, timezone

   app = Flask(__name__)
   CORS(app)

   @app.route('/')
   def home():
       return jsonify({"status": "online", "service": "Webhook Manus GPT"})

       @app.route('/receber-instrucao-gpt', methods=['POST'])
       def receber():
           dados = request.get_json()
               return jsonify({
                       "status": "recebida",
                               "delivery_id": str(uuid.uuid4()),
                                       "message": "Instrução recebida com sucesso",
                                               "timestamp": datetime.now(timezone.utc).isoformat()
                                                   })

                                                   if __name__ == '__main__':
                                                       app.run(host='0.0.0.0', port=int(os.environ.get('PORT', 10000)))
