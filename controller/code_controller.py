from flask import Blueprint, jsonify, request

from service.code_translate_service import translate_function

controller_bp = Blueprint('controller', __name__)


@controller_bp.route('/translate', methods=['POST'])
def translate():
    input_language = request.args.get('inputLanguage')
    output_language = request.args.get('outputLanguage')

    input_text = request.get_json().get('inputText')

    result = translate_function(input_text, input_language, output_language)

    return jsonify({"result": result})
