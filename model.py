from schema import Schema, And, Use, Optional, SchemaError

def check(conf_schema, conf):
    try:
        conf_schema.validate(conf)
        return True
    except SchemaError:
        return False

def consoleSchema():
    return Schema({
        'sessionID': And(Use(str)),
        'type': And(Use(str)),
        'timestamp': And(Use(str)),
        'event': And(Use(str))
    })


def recordingSchema():
    return Schema({
        'sessionID': And(Use(str)),
        'type': And(Use(str)),
        'timestamp': And(Use(str)),
        'event': {
            'type': And(Use(str)),
            'data': And(Use(object)),
            'timestamp': And(Use(str))
        }
    })

def performanceSchema():
    return Schema({
        'sessionID': And(Use(str)),
        'type': And(Use(str)),
        'timestamp': And(Use(str)),
        'event': {
            'name': And(Use(str)),
            'entryType': And(Use(str)),
            'startTime': And(Use(int)),
            'duration': And(Use(int)),
            'initiatorType': And(Use(str)),
            'nextHopProtocol': And(Use(str)),
            'workerStart': And(Use(int)),
            'redirectStart': And(Use(int)),
            'redirectEnd': And(Use(int)),
            'fetchStart': And(Use(int)),
            'domainLookupStart': And(Use(int)),
            'domainLookupEnd': And(Use(int)),
            'connectStart': And(Use(int)),
            'connectEnd': And(Use(int)),
            'secureConnectionStart': And(Use(int)),
            'requestStart': And(Use(int)),
            'responseStart': And(Use(int)),
            'responseEnd': And(Use(int)),
            'transferSize': And(Use(int)),
            'encodedBodySize': And(Use(int)),
            'decodedBodySize': And(Use(int)),
            'serverTiming': And(Use(str))
        }
    })

def locationSchema():
    return Schema({
        'sessionID': And(Use(str)),
        'type': And(Use(str)),
        'timestamp': And(Use(str)),
        'event': {
            'origin': And(Use(str))
        }
    })

def screenSchema():
    return Schema({
        'sessionID': And(Use(str)),
        'type': And(Use(str)),
        'timestamp': And(Use(str)),
        'event': {
            'width': And(Use(int)),
            'height': And(Use(int))
        }
    })

def organizationSessionSchema():
    return Schema({
        'name': And(Use(str)),
        'version': And(Use(str)),
        'os': And(Use(str)),
        'url': And(Use(str)),
        'code': And(Use(str)),
        'tokenId': And(Use(str))
    })


