from flask import Flask
from routes import user_bp
from flask_cors import CORS

app = Flask(__name__)
CORS(app)
app.config['JSON_SORT_KEYS'] = False
app.register_blueprint(user_bp, url_prefix='/api/users')

@app.route('/')
def index():
    return {"message": "Clusterverse Backend is Live 🎉"}

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=10000)
