from flask import Blueprint, request, jsonify
from .service import fake_login

auth_bp = Blueprint("auth", __name__)

@auth_bp.post("/login")
def login():
    data = request.get_json()

    if not data:
        return jsonify({ "error": "JSON required"}), 400

    username = data.get("username")
    password = data.get("password")

    token = fake_login(username=username, password=password)
    if not token:
        return jsonify({ "error": "Invalid credentials" }), 401

    return jsonify({ "token": token })