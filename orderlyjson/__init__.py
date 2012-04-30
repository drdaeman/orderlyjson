import orderly_json
import validictory
import json

def parse(orderly_string):
    """Parses an Orderly-JSON string, and returns a JSON-Schema object"""
    return orderly_json.parseString(orderly_string)

def parseFile(path):
    """Parses an Orderly-JSON file, and returns a JSON-Schema object"""
    return orderly_json.parseFile(path)

def validate(json_object, orderly_object):
    """Validates the JSON string with an Orderly definition"""
    if type(orderly_object) is str:
        orderly_object = parse(orderly_object)
    validictory.validate(json_object, orderly_object)


def test():
    example_orderly = """
    object {
        string name;
        string description?;
        string homepage /^http:/;
        integer {1500,3000} invented;
    }*;
    """

    example_json = """
    {
        "name": "orderly",
        "description": "A schema language for JSON",
        "homepage": "http://orderly-json.org",
        "invented": 2009
    }
    """
    example_json = json.loads(example_json)
    schema = parse(example_orderly)
    try:
        validate(example_json, schema)
    except:
        pass
