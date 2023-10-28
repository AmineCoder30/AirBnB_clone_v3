#!/usr/bin/python3
"""
Index model holds the endpoint (route)
"""
from api.v1.views import app_views, storage
from flask import jsonify


@app_views.route('/status/')
def status():
    """Example endpoint returns status
    returns the current status of the API
    """
    return jsonify({"status": "OK"})


@app_views.route('/stats/')
def stats():
    """ Returns the number of each instance type """
    return jsonify(amenities=storage.count("Amenity"),
                   cities=storage.count("City"),
                   places=storage.count("Place"),
                   reviews=storage.count("Review"),
                   states=storage.count("State"),
                   users=storage.count("User"))
