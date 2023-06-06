import json
import pytest
from main import app
from consts import SourceTypes, TemplateNames


class TestAPI:

    def test_api_validation_template_not_exist(self):
        request_as_dict = {"source_type": SourceTypes.STRING.value, "input_value": "input_value",
                           "output_file": "output_file", "template": "invalid template"}
        response = app.test_client().post('/html-to', json=request_as_dict)
        assert response.status_code == 403

    def test_api_validation_wrong_source_value(self):
        request_as_dict = {"source_type": "invalid type", "input_value": "input_value",
                           "output_file": "output_file", "template": TemplateNames.SIMPLE.value}
        response = app.test_client().post('/html-to', json=request_as_dict)
        expected_data = "'invalid type' is not one of ['string', 'url', 'file']"
        response_data = json.loads(response.data).get('message')[0]
        assert response.status_code == 403
        assert response_data == expected_data

    def test_api_validation_no_source_value(self):
        request_as_dict = {"input_value": "input_value",
                           "output_file": "output_file", "template": TemplateNames.SIMPLE.value}
        response = app.test_client().post('/html-to', json=request_as_dict)
        expected_data = "'source_type' is a required property"
        response_data = json.loads(response.data).get('message')[0]
        assert response.status_code == 403
        assert response_data == expected_data

    def test_api_validation_no_input(self):
        request_as_dict = {"source_type": SourceTypes.STRING.value,
                           "output_file": "output_file", "template": TemplateNames.SIMPLE.value}
        response = app.test_client().post('/html-to', json=request_as_dict)
        expected_data = "'input_value' is a required property"
        response_data = json.loads(response.data).get('message')[0]
        assert response.status_code == 403
        assert response_data == expected_data

    def test_convert_from_string_create_file(self):
        request_as_dict = {"source_type": SourceTypes.STRING.value, "input_value": "input_value",
                           "output_file": "output_file", "template": TemplateNames.SIMPLE.value}
        response = app.test_client().post('/html-to', json=request_as_dict)
        expected_data = b"process complete a file was created and stored locally"
        assert response.status_code == 200
        assert response.data == expected_data

    def test_convert_from_file(self):
        with open('test-html', 'rb') as f:
            data = f.read()
            request_as_dict = {"source_type": SourceTypes.FILE.value, "input_value": data.decode('unicode_escape'),
                               "template": "simple"}
            res = app.test_client().post('/html-to', json=request_as_dict)
            assert res.status_code == 200

    def test_convert_from_url_bytes_output(self):
        request_as_dict = {"source_type": SourceTypes.URL.value, "input_value": "http://google.com",
                           "template": "simple"}
        response = app.test_client().post('/html-to', json=request_as_dict)
        assert response.status_code == 200
        assert type(response.data) == bytes
