from flask import Flask , render_template
from api.routes import api_blueprint
import os

app = Flask(__name__)

app.register_blueprint(api_blueprint , url_prefix="/api")

@app.route("/")
def home():
    return render_template("templates/index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port = 5000 , debug=True)