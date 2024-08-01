from flask import Flask
from flask_cors import CORS

from controller.code_controller import controller_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(controller_bp)

if __name__ == '__main__':
    app.run(debug=True)
