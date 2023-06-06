from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from consts import SourceTypes, TemplateNames
from templates_handler import get_template_names

conversions_schema = {
    "type": "object",
    "properties": {
        "input_value": {
            "type": "string",
        },
        "output_file": {
            "type": "string",
            "pattern": "[^.]+"
        },
        "source_type": {
            "default": "string",
            "enum": [source_type.value for source_type in SourceTypes]
        },
        "template": {
            "type": "string",
        }
    },

    "required": ["input_value", "source_type"]
}


class ConvertInput(Inputs):
    json = [JsonSchema(schema=conversions_schema)]


def validate_convert_request(request):
    inputs = ConvertInput(request)
    if inputs.validate():
        return None
    else:
        return inputs.errors
