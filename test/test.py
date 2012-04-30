import json
from orderlyjson import parse, validate

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
    validate(example_json, schema)
