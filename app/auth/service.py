import jwt
import datetime
from flask import current_app

FAKE_USER = {
    "username": "martin",
    "password": "1234"
}

def fake_login(username, password):
    if username != FAKE_USER["username"] or password != FAKE_USER["password"]:
        return None
    
    payload = {
        "sub": username,
        "exp": datetime.datetime.utcnow() + datetime.timedelta(hours=2)
    }

    token = jwt.encode(payload=payload, key=current_app.config["SECRET_KEY"], algorithm="HS256")

    return token
