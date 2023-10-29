#!/usr/bin/python3
"""
Flask route that returns json status response
"""
from api.v1.views import app_views
from flask import jsonify, request
from models import storage


@app_views.route('/status', strict_slashes=False,  methods=['GET'])
def status():
    """
    Function for status route that returns the status
    """
    if request.method == 'GET':
        resp = {"status": "OK"}
        return jsonify(resp)


@app_views.route('/stats', strict_slashes=False, methods=['GET'])
def stats():
    """
    funtion to return the count of all class objects
    """
    if request.method == 'GET':
        response = {}
        PLURALS = {
            "Amenity": "amenities",
            "City": "cities",
            "Place": "places",
            "Review": "reviews",
            "State": "states",
            "User": "users"
        }
        for key, value in PLURALS.items():
            resonse[value] = storage.count(key)
        return jsonify(response)
