from flask import Flask

from controller.code_controller import controller_bp

app = Flask(__name__)

app.register_blueprint(controller_bp)

if __name__ == '__main__':
    app.run(debug=True)
