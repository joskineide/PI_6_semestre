from flask import Flask, request
from flask_restful import Resource, Api
from pymongo import MongoClient
import model

mongo_url = "mongodb://teste123:teste123@ds141188.mlab.com:41188/heroku_2h0prhnv?retryWrites=false"

mongo_db = MongoClient(mongo_url).heroku_2h0prhnv

mongo_collection_session = mongo_db.session

app = Flask(__name__)
api = Api(app)


@app.route('/api/sessions/<code>', methods=['POST'])
def createSession(code):
    try:
        session = request.get_json()
        session["code"] = code
        session["url"] = request.remote_addr

        mongo_response = mongo_collection_session.insert_one(session)
        return str(mongo_response.inserted_id), 201

    except Exception as e: 
        return "Error occured", 500


@app.route('/api/sessions/<sessionId>/<code>/events', methods=['POST'])
def putEvents(sessionId, code):
    try:

        events = request.get_json()

        bulkBody = []

        for event in events:
            typeRaw = event["type"].split(".")
            event_type = "network" if typeRaw[0] == "xhr" or typeRaw[0] == "fetch" else typeRaw[0]
            session = {
                "sessionID": sessionId,
                "code": code,
                **event
            } 
            bulkBody.append({
                "index": {
                    "_index": "besouro-" + event_type,
                    "_type": event_type
                }
            })
            mongo_collection_event = mongo_db[event_type].insert_one(session)
            bulkBody.append(session)

        return "success", 200

    except Exception as e: 
        return "Error occured", 500


@app.route('/healthCheck', methods=['GET'])
def getHealthCheck():
    return "LIVE"






app.run(port=5002)




