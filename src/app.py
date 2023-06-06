from flask import Flask, request, jsonify, Response
from flask_cors import CORS
from ocr import OCR
import json

app = Flask(__name__)
CORS(app)

@app.route('/', methods=['GET'])
def root():
    return response(True, 'Hello World!')

@app.route('/', methods=['POST'])
@app.route('/upload', methods=['POST'])
def upload_file():
    try:
        data = request.get_json()
        link = data["link"]
        if link:
            ocr = OCR()
            return Response(json.dumps(ocr.main(link), sort_keys=False), mimetype='application/json')
        else:
            return response(False, 'É necessário enviar um link no body da requisição!')
    except Exception as e:
        return response(False, str(e))

def response(success, data):
    if(success):
        response = {'success': True, 'data': data}
    else:
        response = {'success': False, 'error': data}

    return Response(json.dumps(response, sort_keys=False), mimetype='application/json')

if __name__ == '__main__':
    app.run()