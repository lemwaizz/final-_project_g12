from flask import Flask

def create_app():
    app = Flask(__name__)

    @app.route('/')
    def home():
        return 'Hello, World!'

    @app.route('/test')
    def test():
        return 'This is a test route.'

    return app
