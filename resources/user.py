from flask import Flask
from flask_restx import Resource

from server.instance import server
from models.user import user
from services.user import user_service

app, api = server.app, server.api
user_ns = api.namespace('users', description='User operations')


@user_ns.route('')
class UserList(Resource):
    @user_ns.marshal_list_with(user)
    def get(self):
        return user_service.get_all()

    @user_ns.expect(user, validate=True)
    @user_ns.marshal_with(user)
    def post(self):
        user_service.create(api.payload)
        return api.payload


@user_ns.route('/<int:user_id>')
class User(Resource):
    @user_ns.marshal_with(user)
    def get(self, user_id):
        return user_service.get(user_id)
