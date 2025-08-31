from flask import Flask
from flask_cors import CORS
from routes.user_routes import user_bp
from database import init_db

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_bp, url_prefix='/users')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)