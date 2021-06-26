from flask_restx import fields
from server.instance import server

user = server.api.model('User', {
    'id': fields.Integer(description='Id'),
    'first_name': fields.String(required=True, min_length=3, max_length=200, description='User first name'),
    'last_name': fields.String(required=True, min_length=3, max_length=200, description='User last name')
})
