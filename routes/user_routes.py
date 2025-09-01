from flask import Blueprint, request, jsonify
from database import get_db_connection

user_bp = Blueprint('user_bp', __name__)

@user_bp.route('/ping', methods=['GET'])
def ping():
    return "✅ Server is running", 200

@user_bp.route('/users', methods=['GET'])
def get_users():
    conn = get_db_connection()
    users = conn.execute('SELECT * FROM users').fetchall()
    conn.close()
    return jsonify([dict(u) for u in users])

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    name = data.get('name')
    email = data.get('email')
    conn = get_db_connection()
    conn.execute('INSERT INTO users (name, email) VALUES (?, ?)', (name, email))
    conn.commit()
    conn.close()
    return jsonify({'message': 'User created'}), 201