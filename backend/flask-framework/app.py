import json
from flask import Flask, request, make_response
from translate_service import decipher_prescription as decipher, all_prescription_keys

#
app: str = Flask(__name__)

@app.get('/')
def get_prescription_translation():
    try:
        codes = request.args.get("codes", None)
        if codes is None:
            raise ValueError('codes parameter missing')
        output = decipher(codes)
        response = make_response(json.dumps(output), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except ValueError as error:
        return make_response(str(error), 400)
    except Exception as base_error:
        return make_response(str(base_error), 400)

@app.get('/keys')
def get_prescription_sig_keys():
    try:
        response = make_response(json.dumps(all_prescription_keys), 200)
        response.headers['Access-Control-Allow-Origin'] = '*'
        return response
    except Exception as base_error:
        return make_response(str(base_error), 400)
