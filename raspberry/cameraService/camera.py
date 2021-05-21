# -*- coding: utf-8 -*-

from flask import jsonify
from flask import request
from flask import Blueprint
from flask import session
from werkzeug.utils import secure_filename
from raspberry import mongo
import json, os

camera_micro_service = Blueprint("camera_micro_service", __name__)


@camera_micro_service.route('/api/camera_entry', methods=['POST'])
def camera_entry():
    message = {"type": "", "data": ""}
    try:
        requests = request.json
        mongo.db.plates.update_one(
                {"plate": "" },
                { "$set": {"plate": requests['infoplate']['Plate']}}
            )
        print(requests['infoplate']['Plate'])
        message["type"] = 'true' 
        message["data"] = requests
        return jsonify(message),200
    except Exception as exception: 
        print("======CREATE_REQUEST=====")
        print(exception)
        return '',500

@camera_micro_service.route('/api/camera_exit', methods=['POST'])
def camera_exit():
    message = {"type": "", "data": ""}
    try:
        requests = request.json
        session['plate_exit'] = requests['infoplate']['Plate']
        print(session['plate_exit'])
        message["type"] = 'true' 
        message["data"] = requests
        return jsonify(message),200
    except Exception as exception: 
        print("======CREATE_REQUEST=====")
        print(exception)
        return '',500

@camera_micro_service.route('/api/camera_plate_entry', methods=['GET'])
def camera_plate_entry():
    message = {"type": "", "data": ""}
    try:
        plate = list(mongo.db.plates.find({}))[0]
        print(plate)
        if plate['plate']: 
            message["type"] = 'true'  
            message["data"] = plate['plate']
            mongo.db.plates.update_one(
                {"plate": plate['plate'] },
                { "$set": {"plate": ""}}
            )
        else:
            message["type"] = 'false'  
            message["data"] = ""
        return jsonify(message),200
    except Exception as exception: 
        print("======CREATE_REQUEST=====")
        print(exception)
        return '',500

@camera_micro_service.route('/api/camera_plate_exit', methods=['GET'])
def camera_plate_exit():
    message = {"type": "", "data": ""}
    try:
        if 'plate_exit' in session:  
            message["type"] = 'true'  
            message["data"] = session['plate_exit']
        return jsonify(message),200
    except Exception as exception: 
        print("======CREATE_REQUEST=====")
        print(exception)
        return '',500

