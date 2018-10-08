from flask import Flask, jsonify
from flask_pymongo import PyMongo #DOCS: https://flask-pymongo.readthedocs.io/en/latest/

#Connects to mongo db from flask
app = Flask(__name__)
app.config['MONGO_DBNAME'] = 'openuniverse'
app.config["MONGO_URI"] = "mongodb://localhost:27017/openuniverse"
mongo = PyMongo(app)


@app.route("/")
def hello():
	return "Hello World!\nThis is openuniverse.me API"


@app.route("/projects", methods =['GET'])
def get_all_projects():
	results = []
	for r in mongo.db.projects.find():
		results.append({'id':r["project_id"], 'name':r["name"], 'url':r["github_url"]})
	return jsonify({'results': results})

