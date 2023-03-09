from pathlib import Path

import pytest

from consts import SourceTypes
from html_to_pdf_converter_service import convert
from unittest.mock import patch



class TestConverter:
    foldername_for_outputs = "test-outputs"

    def test_convert_from_string(self):
        result = convert(SourceTypes.STRING, input_value="<h1>Test<h1>",
                         output_file='output')

        expected_result = {'result': 'process complete a file was created'}
        assert result == expected_result

    def test_convert_from_file(self):
        result = convert(SourceTypes.STRING, input_value="<h1>Test<h1>",
                         output_file='output')

        expected_result = {'result': 'process complete a file was created'}
        assert result == expected_result

    def test_convert_from_url(self):
        result = convert(SourceTypes.STRING, input_value="http://google.com",
                         output_file='output')

        expected_result = {'result': 'process complete a file was created'}
        assert result == expected_result

    def test_convert_from_string_no_file_created(self):
        result = convert(SourceTypes.STRING, input_value="<h1>Test<h1>", )
        assert type(result.get('result')) == bytes

    def test_convert_invalid_template(self):
        result = convert(SourceTypes.STRING, input_value="<h1>Test</h1>", template="fake")
        expected_error = {'error': 'FileNotFoundError'}
        assert result == expected_error

    @patch("consts.MAX_SUPPORTED_FILE_COUNT", 1)
    @patch("html_to_pdf_converter_service.get_outputs_folder_name", Path(__file__).parent.absolute() / "test-outputs")
    def test_cannot_create_more_than_max_files(self):
        convert(SourceTypes.STRING, input_value="http://google.com",
                output_file='output')
        result = convert(SourceTypes.STRING, input_value="<h1>Test<h1>",
                         output_file='output')

        expected_result = {'error': 'StorageOverload'}
        assert result == expected_result

    @classmethod
    def teardown_class(cls):
        import os
        files = os.listdir( (str(Path(__file__).parent.absolute() / cls.foldername_for_outputs)))
        for f in files:

            os.remove(str(Path(__file__).parent.absolute() / cls.foldername_for_outputs)+ "\\"+f)
