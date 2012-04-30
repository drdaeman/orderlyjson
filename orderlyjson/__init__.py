import OrderlyJSONLexer, OrderlyJSONParser
import validictory
import json

def validate(json_object, orderly_object):
    """Validates the JSON object with an Orderly definition"""
    if type(orderly_object) in (str, unicode):
        orderly_object = parse(orderly_object)
    if type(json_object) in (str, unicode):
        json_object = json.loads(json_object)
    validictory.validate(json_object, orderly_object)

def parseStream(char_stream):
    lexer = OrderlyJSONLexer.OrderlyJSONLexer(char_stream)
    tokens = OrderlyJSONParser.CommonTokenStream(lexer)
    parser = OrderlyJSONParser.OrderlyJSONParser(tokens)
    result = parser.orderly_schema()
    return result

def parseString(string):
    """Parses an Orderly-JSON string, and returns a JSON-Schema object"""
    result = parseStream(OrderlyJSONLexer.ANTLRStringStream(string))
    return result[0].get_object()

def parseFile(path):
    """Parses an Orderly-JSON file, and returns a JSON-Schema object"""
    result = parseStream(OrderlyJSONLexer.ANTLRFileStream(path))
    return result[0].get_object()

parse = parseString
