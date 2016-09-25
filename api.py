from flask_restful import Resource
from flask_restful.reqparse import RequestParser

class HelloWorld(Resource):
	def get(self): #example of api
		return "hello world!"
class UserLogin(Resource):
	def __init__(self):
		self.reqparse = RequestParser()
		self.reqparse.add_argument('name', type=str, required= True, help="GaTech Username is required to login", location='json')
		self.reqparse.add_argument('number', type=str, required= True, help="Password is required to login", location='json')
        self.reqparse.add_argument('date', type=str, required= True, help="Password is required to login", location='json')
		super(UserLogin, self).__init__()

	def post(self):
		args = self.reqparse.parse_args()
		username = args['username']
		password = args['password']
