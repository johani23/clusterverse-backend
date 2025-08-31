from flask import Flask
from app.routes.main import main_bp
from app.models.models import db
import os

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'clusterverse_secret_key'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///clusterverse.db'
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    db.init_app(app)
    app.register_blueprint(main_bp)

    with app.app_context():
        db.create_all()

    return app

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 10000))
    app = create_app()
    app.run(host='0.0.0.0', port=port)