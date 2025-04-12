from flask import Flask, request, jsonify
import importlib.util
import os


app = Flask(__name__)

@app.route('/')
def index():
    return "Servidor de Automação Online"

@app.route('/executar/<nome_automacao>', methods=['GET','POST'])
def executar_automacao(nome_automacao):
    caminho = f'automacoes/{nome_automacao}.py'

    if not os.path.exists(caminho):
        return jsonify({"erro": "Automação não encontrada"}), 404
    
    spec = importlib.util.spec_from_file_location("modulo_automacao", caminho)
    modulo = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(modulo)


    if request.method == 'POST':
        if request.is_json:
            args = request.json.get("args", [])
        else:
            return jsonify({"erro": "Requisição POST deve ser JSON"}), 415
    else:
        args = []
        

    resultado = modulo.executar(args)

    return jsonify({"resultado": resultado})

if __name__ == '__main__': 
    from os import environ
    port = int(environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
    