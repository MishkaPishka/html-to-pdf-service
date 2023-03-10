from flask_inputs import Inputs
from flask_inputs.validators import JsonSchema
from consts import SourceTypes, TemplateNames

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
            "enum":  [template_type.value for template_type in TemplateNames]
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
