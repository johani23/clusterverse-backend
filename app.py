    from flask import Flask
from flask_cors import CORS

from routes.user_routes import user_routes  # استيراد البلوبّرينت

app = Flask(__name__)
CORS(app)

# تسجيل البلوبّرينت
app.register_blueprint(user_routes)

if __name__ == '__main__':
    app.run(debug=True)
