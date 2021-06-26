from flask import Response, jsonify
import jwt
from config.environment import jwt_secret
import datetime

from server.instance import server
from services.user import user_service

app, api = server.app, server.api


@app.route('/auth/login', methods=["POST"])
def login():
    try:
        user = api.payload
        validated_user = user_service.validate_user(user)
        validated_user.update({"exp": datetime.datetime.utcnow() + datetime.timedelta(seconds=30)})
        token = jwt.encode(validated_user, jwt_secret, algorithm="HS256")
        return jsonify({"token": token})
    except RuntimeError:
        return Response('Authorization failed', mimetype='text/plain', status=401)
