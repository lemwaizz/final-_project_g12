print("Starting run.py")

from flask import Flask, render_template
import logging

print("Imported Flask and other modules")

def create_app():
    logging.basicConfig(level=logging.DEBUG)
    print("Creating Flask app")
    
    app = Flask(__name__, static_folder='static', template_folder='templates')

    @app.route('/register')
    def register():
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

print("Created app")

if __name__ == "__main__":
    print("Running app")
    app.run(debug=True)
