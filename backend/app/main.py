from flask import Flask ,jsonify

from api.routes import api_blueprint


# flask app
def create_app():
    app = Flask(__name__)
    app.register_blueprint(api_blueprint , url_prefix="/api")
    return app

if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port = 5000 , debug=True)

