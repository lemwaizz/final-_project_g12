from flask import Flask, render_template
import logging

def create_app():
    logging.basicConfig(level=logging.DEBUG)
    print("Creating Flask app")
    
    app = Flask(__name__, static_folder='static', template_folder='app/templates')

    @app.route('/')
    def home():
        return render_template('Registration.html')

    @app.route('/login')
    def login():
        return render_template('Login.html')

    @app.route('/test')
    def test():
        return 'This is a test route.'

    app.logger.debug('App created successfully!')
    print('App created successfully!')

    return app

app = create_app()

if __name__ == "__main__":
    app.run(debug=True)

