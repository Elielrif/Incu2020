from flask import Flask, render_template, request, json, jsonify
from flask_pymongo import PyMongo
from pymongo import ReturnDocument
from bson import json_util

app = Flask(__name__)
app.secret_key = 'xyz'

app.config["MONGO_URI"] = "mongodb://svetlana:cisco123@localhost:27017/Device_Configuration"

json.dumps = json_util.dumps

mongo = PyMongo(app)


@app.route('/<Switch_name>/interfaces.html', methods=['GET'])
def get_switch_name(Switch_name):
    result = mongo.db.Interfaces.find({"Switch_name": Switch_name})
    return render_template('interfaces.html', result=result)


@app.route('/<Switch_name>/<Interface_Name>/details.html', methods=['GET'])
def get_switch_name_interface(Switch_name, Interface_Name):
    result = mongo.db.Interfaces.find({"Switch_name": Switch_name, "Interface_Name": Interface_Name.replace('.', '/')})
    return render_template('interfaces.html', result=result)


@app.route('/<Switch_name>/interfaces.JSON', methods=['GET'])
def get_switch_name_json(Switch_name):
    result = mongo.db.Interfaces.find({"Switch_name": Switch_name})
    return jsonify(result), 200


@app.route('/<Switch_name>/<Interface_Name>/details.JSON', methods=['GET'])
def get_switch_name_json_detail(Switch_name, Interface_Name):
    result = mongo.db.Interfaces.find({"Switch_name": Switch_name, "Interface_Name": Interface_Name.replace('.', '/')})
    return jsonify(result), 200


@app.route('/<Switch_name>/<ObjectId:_id>', methods=['PATCH'])
def patch_switch_name_interface(Switch_name, _id):
    payload = request.get_json()
    if payload:
        result = mongo.db.Interfaces.find_one_and_update(
            {"Switch_name": Switch_name, "_id": _id},
            {'$set': payload},
            return_document=ReturnDocument.AFTER
        )
        return jsonify(result), 200
    return "Error!", 500


if __name__ == '__main__':
    app.run()
