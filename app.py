from flask import Flask
from flask_cors import CORS
from routes.user_routes import user_bp

app = Flask(__name__)
CORS(app)

app.register_blueprint(user_bp)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)  # أو أي بورت تطلبه Render
