from flask import Flask, jsonify, request, Response

from aws_connector import HAS_AWS_SUPPORT, REGION
from consts import SourceTypes
from html_to_pdf_converter_service import convert
from errors.invalid_request_error import InvalidRequest
from templates_handler import save_template
from validations import validate_convert_request

app = Flask(__name__)


@app.errorhandler(InvalidRequest)
def handle_invalid_usage(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.before_request
def before_request():
    is_convert_request = request.base_url.endswith("/html-to")
    if request.method == "POST" and is_convert_request:
        validation_errors = validate_convert_request(request)
        if validation_errors:
            raise InvalidRequest(validation_errors)


@app.route("/html-to", methods=["POST"])
def handle_html_to_pdf():
    response_data = convert(SourceTypes(request.json.get("source_type")), input_value=request.json.get("input_value"),
                            output_file=request.json.get("output_file"), template=request.json.get("template"))

    if response_data.get("result"):
        return Response(response_data.get("result"), mimetype="application/pdf")

    return jsonify(response_data.get("error")), 500


@app.route("/example", methods=["GET"])
def generate_example_template():
    html = "<html><body><h1>Simple Template</h1><div>Example</div><div><p>p example </p></div></body></html>"
    response_data = convert(SourceTypes.STRING, input_value=html, template=dict(request.args).get("type", "simple"))

    if response_data.get("result"):
        return Response(response_data.get("result"), mimetype="application/pdf")
    return jsonify(response_data.get("error")), 500


@app.route("/upload_template", methods=["POST"])
def upload_template():
    template_data = request.json.get("content")
    template_name = request.json.get("name")
    result = save_template(template_data, template_name)
    if result == template_name:
        return template_name, 200
    else:
        return "Template Upload Error", 400


@app.route("/get_templates", methods=["GET"])
def get_template_names():
    import templates_handler
    return jsonify(templates_handler.get_template_names()), 200


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=False, use_reloader=False)
