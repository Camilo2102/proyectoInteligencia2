from flask import Blueprint, jsonify, request

controller_bp = Blueprint('controller', __name__)


@controller_bp.route('/translate', methods=['POST'])
def translate():
    inputLanguage = request.args.get('inputLanguage')
    outputLanguage = request.args.get('outputLanguage')

    if inputLanguage:
        message = f"Hello, World in {inputLanguage}!"
    else:
        message = "Hello, World!"
    return jsonify({"message": message})
