import json
import jsonschema
from jsonschema import validate

ReadSchema={"$schema": "http://json-schema.org/schema#", "type": "object", "properties": {"study_id": {"type": "string","minLength": 1, 
"maxLength": 50}, "block_type": {"type": "string", "oneOf":[{"pattern": "^[A-Z]"}, {"pattern": "^[a-z]"}], "enum": ["CHECKBOX"]}, 
"sequence": {"type": "integer","minimum": 1, "exclusiveMinimum":0, "maximum":10, "exclusiveMaximum":11}, "block_properties": {"type": "object", 
"properties": {"question": {"type": "string"}, "options": {"type": "array", "items": {"type": "object", "properties": {"option_text": 
{"type": "string"}, "option_id": {"type": "string"}}, "required": ["option_text"]}, "minItems": 1, "maxItems":4, "uniqueItems": True, 
"additionalItems":False}, "response_required": {"type": "boolean"}, "randomize": {"type": "boolean"}, "none_of_the_above": {"type": "boolean"}, 
"others": {"type": "boolean"}, "all_of_the_above": {"type": "boolean"}}, "maxProperties":15, "minProperties":1, 
"required": ["all_of_the_above", "none_of_the_above", "options", "others", "question", "randomize", "response_required"]}}, 
"required": ["block_properties", "block_type", "sequence", "study_id"]}


def validate2(val):
    
        try:
            word1=json.load(open('{}'.format(val)))
            validate(instance=word1, schema=ReadSchema)
        except Exception as e:
            return e
        return True

val="C:\swapnil\json_file\Validate\Sample_json_data.json"
print(validate2(val))
print()
