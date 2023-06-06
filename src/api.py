from flask import Flask, request, jsonify
from flask_cors import CORS
from ocr import OCR

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def root():
    return response(True, 'Hello World!')

@app.route('/', methods=['POST'])
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        data = request.json
        link = data.get('link')
        if link:
            ocr = OCR()
            return jsonify(ocr.main(link))
        else:
            return response(False, 'É necessário enviar um link no body da requisição!')
    except Exception as e:
        return response(False, "É necessário enviar um link no body da requisição! Erro:" + str(e))

def response(success, data):
    if(success):
        return jsonify({'success': True, 'data': data})
    else:
        return jsonify({'success': False, 'error': data})

if __name__ == '__main__':
    app.run()