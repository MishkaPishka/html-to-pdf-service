from typing import Union
import os
import pdfkit

import consts
from errors.storage_overload_error import StorageOverload
from consts import SourceTypes
from pathlib import Path

PATH_TO_HTML_TO_PDF = os.environ.get("PATH_TO_HTML_TO_PDF", "C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
CONFIG = pdfkit.configuration(wkhtmltopdf=PATH_TO_HTML_TO_PDF)

mapping = {SourceTypes.STRING: pdfkit.from_string, SourceTypes.URL: pdfkit.from_url, SourceTypes.FILE: pdfkit.from_string}


def parse_output_file_name(output_file: str):
    try:
        if output_file:
            return output_file if output_file.endswith(".pdf") else output_file + ".pdf"
    except Exception as e:
        print("Invalid output file format", e.__repr__)
    return False


def get_outputs_folder_name():
    return Path(__file__).parent.absolute() / consts.OUTPUTS_FOLDER_NAME


def can_store_more_files():
    # https://pynative.com/python-count-number-of-files-in-a-directory/
    # folder path
    dir_path = get_outputs_folder_name()
    count = 0
    # Iterate directory
    for path in os.listdir(dir_path):
        # check if current path is a file
        if os.path.isfile(os.path.join(dir_path, path)):
            count += 1
    if count < consts.MAX_SUPPORTED_FILE_COUNT:
        return True
    return False


def set_output_path_if_needed(params, output_file):
    output_file = parse_output_file_name(output_file)
    if output_file:
        if can_store_more_files():
            params["output_path"] = get_outputs_folder_name() / output_file
            print(params["output_path"])
        else:
            print("Could not store more files")
            raise StorageOverload("Can't store more files to server")
    return params


def convert(source_type: SourceTypes, input_value, output_file: str = "", template: str = "") -> Union[bytes, bool]:
    try:

        input_param_name = SourceTypes.URL.value if source_type == SourceTypes.URL else "input"
        input_value = bytes(input_value, 'unicode_escape') if source_type == SourceTypes.FILE.value else input_value
        params = {input_param_name: input_value, "configuration": CONFIG}
        if source_type in [SourceTypes.FILE, SourceTypes.STRING] and template:
            params["css"] = os.path.join(consts.TEMPLATES_FOLDER_NAME, consts.TEMPLATES_MAPPING.get(template, ""))

        set_output_path_if_needed(params, output_file)
        convert_result = mapping.get(source_type)(**params)
        if convert_result is True:
            return {"result": "process complete a file was created"}
        return {"result": convert_result}

    except (FileNotFoundError, IOError, OSError, StorageOverload) as e:
        print(e.__repr__)
        return {"error": type(e).__name__}
