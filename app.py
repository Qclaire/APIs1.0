from flask import Flask, request
from flask_restful import Resource, Api
from sqlalchemy import create_engine
from json import dumps
from flask_jsonpify import jsonify

db_connect = create_engine('sqlite:///chinook.db') # link to the db

app = Flask(__name__) # initailise a flask app
api = Api(app) # initialise an API on the app


class Employees(Resource): # a class extending the Resource class
	def get(self): # method representing a get request
		conn = db_connect.connect() # connect to the db
		query = conn.execute("select * from employees")# make a db query
		return {'employees':[i[0] for i in query.fetchall()]} # return results

class Tracks(Resource):
	
	def get(self):
		conn = db_connect.connect()
		query = conn.execute("select trackid, name, composer, unitprice from tracks;")
		result = {'data': [dict(zip(query.keys(), i)) for i in query.cursor] }
		return jsonify(result)

class Employees_Name(Resource):		
	
	def get(self, id):
		# print(employee_id)
		# conn = db_connect.connect()
		# query = conn.execute('select * from employees where EmployeeId=%d'%int(employee_id))
		# result = {'data': [dict(zip(tuple(query.keys()), i)) for i in query.cursor]}
		# return jsonify(result)
		return id


api.add_resource(Employees, '/employees')
api.add_resource(Tracks,'/tracks')
api.add_resource(Employees, '/employee/<id>', endpoint='employee')


if __name__ == '__main__':
	app.run(debug=True)

